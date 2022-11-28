import time
from threading import Thread
from typing import Dict
from ICoolingSystem import ICoolingSystem, ICoolingSystemObserver


class TypeBCoolingSystem(Thread, ICoolingSystem):
    """
    Concrete implementation of the ICoolingSystem interface for the type A cooling system.
    """

    def __init__(self, nickname):
        Thread.__init__(self)
        self._nickname = nickname
        self.dead_band = 0.5
        self._current_room_temperature = 0.0
        self._desired_room_temperature = 22.0
        self._is_cooling = False
        self._is_cooling_thread_running = False
        self._observers = []

    def attach(self, observer: ICoolingSystemObserver) -> None:
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer: ICoolingSystemObserver) -> None:
        if observer in self._observers:
            self._observers.remove(observer)

    def notify(self, event: str) -> None:
        for observer in self._observers:
            observer.update(cooling_system=self, event=event)

    def set_desired_room_temperature(self, temperature):
        self._desired_room_temperature = temperature
        # This method should send the command to set the hardware desired room temperature.

    def get_desired_room_temperature(self) -> float:
        return self._desired_room_temperature

    def get_current_room_temperature(self) -> float:
        return self._current_room_temperature

    def turn_on(self):
        self._is_cooling = True
        self.notify("TURN_ON")
        # This method should send the command to the hardware to set the desired room temperature again and turn on.

    def turn_off(self):
        self._is_cooling = False
        self.notify("TURN_OFF")
        # This method should send the command to the hardware to turn off.

    def is_cooling(self) -> bool:
        self._is_cooling

    def run(self):
        self._is_cooling_thread_running = True
        self.notify("PROCESS_START")
        while self._is_cooling_thread_running:
            # This loop should be responsible to capture the hardware states and delivery events to the application.
            time.sleep(0.25)
            # Dummy temperature control
            if self._is_cooling:
                if self._current_room_temperature < self._desired_room_temperature:
                    self._current_room_temperature = self._current_room_temperature + 1
                    self.notify("ROOM_TEMPERATURE_INCREASED")
                if self._current_room_temperature > self._desired_room_temperature:
                    self._current_room_temperature = self._current_room_temperature - 1
                    self.notify("ROOM_TEMPERATURE_DECREASED")
                else:
                    self._is_cooling = False
                    self.notify("AUTO_TURN_OFF")

        self.notify("PROCESS_ENDED")

    def stop(self):
        self._is_cooling_thread_running = False
        if self._is_cooling:
            self.turn_off()
        self.join()
