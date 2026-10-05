from abc import ABC, abstractmethod


class Subscriber(ABC):
    @abstractmethod
    def notify(self, notify_message: str)-> None: ...
