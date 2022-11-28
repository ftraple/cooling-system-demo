import time
from threading import Thread
from ICoolingSystemManager import ICoolingSystemManager, ICoolingSystemManagerObserver
from ICoolingSystem import ICoolingSystem, ICoolingSystemObserver


class CoolingSystemManager(ICoolingSystemManager, ICoolingSystemObserver):

    def __init__(self, nickname):
        self._nickname = nickname
        self._observers = []
        self._cooling_systems = []
        pass

    def attach_observer(self, observer: ICoolingSystemManagerObserver) -> None:
        if observer not in self._observers:
            self._observers.append(observer)

    def detach_observer(self, observer: ICoolingSystemManagerObserver) -> None:
        if observer in self._observers:
            self._observers.remove(observer)

    def notify_observers(self, event: str) -> None:
        for observer in self._observers:
            self._observers.update(self, event)

    def add_cooling_system(self, cooling_system: ICoolingSystem) -> None:
        if cooling_system not in self._cooling_systems:
            if not cooling_system.is_alive():
                cooling_system.start()
            cooling_system.attach(self)
            self._cooling_systems.append(cooling_system)

    def remove_cooling_system(self, cooling_system: ICoolingSystem) -> None:
        if cooling_system in self._cooling_systems:
            cooling_system.detach(self)
            self._cooling_systems.remove(cooling_system)

    def turn_on(self) -> None:
        for cooling_system in self._cooling_systems:
            cooling_system.turn_on()

    def turn_off(self) -> None:
        for cooling_system in self._cooling_systems:
            cooling_system.turn_off()

    def is_cooling(self) -> bool:
        for cooling_system in self._cooling_systems:
            if cooling_system.is_cooling():
                return True
        return False

    def update(self, cooling_system: ICoolingSystem, event: str) -> None:
        print("[{0}] Event: {1}".format(self._nickname, event), flush=True)
