from abc import ABCMeta, abstractmethod
import ICoolingSystem


class ICoolingSystemManagerObserver(metaclass=ABCMeta):
    """
    The Observer interface declares the update method, used by subjects.
    """

    @abstractmethod
    def update(self, event: str) -> None:
        """
        Receive update from subject.
        """


class ICoolingSystemManager(metaclass=ABCMeta):
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
    def attach_observer(self, observer: ICoolingSystemManagerObserver) -> None:
        """
        Attach an observer to the subject.
        """

    @abstractmethod
    def detach_observer(self, observer: ICoolingSystemManagerObserver) -> None:
        """
        Detach an observer from the subject.
        """

    @abstractmethod
    def notify_observers(self, event: str) -> None:
        """
        Notify all observers about an event.
        param event: string to identify the event type
        """

    def add_cooling_system(self, cooling_system: ICoolingSystem) -> None:
        """
        Add a cooling system.
        """

    @abstractmethod
    def remove_cooling_system(self, cooling_system: ICoolingSystem) -> None:
        """
        Remove a cooling system.
        """

    @abstractmethod
    def turn_on(self) -> None:
        """
        Turn on the cooling system manager.
        """

    @abstractmethod
    def turn_off(self) -> None:
        """
        Turn off the cooling system manager.
        """

    @abstractmethod
    def is_cooling(self) -> bool:
        """
        Check if the cooling system manager is working.
        :returns: Return true if the cooling process is running, or false if not.
        """
