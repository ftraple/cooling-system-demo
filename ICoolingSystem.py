from abc import ABCMeta, abstractmethod
from typing import Dict


class ICoolingSystemObserver:
    pass


class ICoolingSystem(metaclass=ABCMeta):
    """
    Interface class to be used as base for implement new cooling systems.
    """

    @abstractmethod
    def __init__(self, nickname):
        """
        Define the class constructor.
        :param nickname: nickname to identify the new instances.
        """

    @abstractmethod
    def attach(self, observer: ICoolingSystemObserver) -> None:
        """
        Attach an observer to the subject.
        """

    @abstractmethod
    def detach(self, observer: ICoolingSystemObserver) -> None:
        """
        Detach an observer from the subject.
        """

    @abstractmethod
    def notify(self, event: str) -> None:
        """
        Notify all observers about an event.
        param event: string to identify the event type
        """

    @abstractmethod
    def set_desired_room_temperature(self, temperature) -> None:
        """
        Set the desired room temperature.
        :param temperature: desired temperature.
        """

    @abstractmethod
    def get_desired_room_temperature(self) -> float:
        """
        Get the desired room temperature.
        returns: Returns the desired temperature.
        """

    @abstractmethod
    def get_current_room_temperature(self) -> float:
        """
        Get current room temperature.
        :returns: Returns the room temperature.
        """

    @abstractmethod
    def turn_on(self) -> None:
        """
        Turn on the cooling system. The cooling system process will start to cooling down or up the room until
        the desired temperature provided.
        """

    @abstractmethod
    def turn_off(self) -> None:
        """
        Turn off the cooling system, that will stop the cooling system process.
        """

    @abstractmethod
    def is_cooling(self) -> bool:
        """
        Check if the cooling system is active.
        :returns: Return true if the cooling system is working, or false if not.
        """


class ICoolingSystemObserver(metaclass=ABCMeta):
    """
    The Observer interface declares the update method, used by subjects.
    """

    @abstractmethod
    def update(self, cooling_system: ICoolingSystem, event: str) -> None:
        """
        Receive update from subject.
        """
