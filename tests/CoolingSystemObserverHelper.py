import time
from ICoolingSystem import ICoolingSystem, ICoolingSystemObserver


class CoolingSystemObserverHelper(ICoolingSystemObserver):

    def __init__(self):
        self.events = {}

    def update(self, cooling_system: ICoolingSystem, event: str) -> None:
        self.events[event] = {"current_room_temperature": cooling_system.get_current_room_temperature()}

    def wait_for_one_event(self, event: str, seconds):
        end_time = time.time() + seconds
        while time.time() < end_time:
            if event in self.events:
                return self.events[event]
            time.sleep(0.25)
        return {}

    def wait_for_events(self, event: str, seconds):
        end_time = time.time() + seconds
        while time.time() < end_time:
            if event in self.events:
                break
            time.sleep(0.1)
        return self.events
