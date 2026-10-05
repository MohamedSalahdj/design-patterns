from dataclasses import dataclass
from subscriber import Subscriber


@dataclass
class User(Subscriber):
    _name: str

    @property
    def name(self) -> str:
        return self._name
    
    @name.setter
    def name(self, new_name: str) -> None:
        self._name = new_name

    def notify(self, notify_message: str)-> None:
        print(f"{self.name} is receiving message: {notify_message}")
