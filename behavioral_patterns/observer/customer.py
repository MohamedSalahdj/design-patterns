from dataclasses import dataclass
from typing import Optional

from subscriber import Subscriber

@dataclass
class Customer(Subscriber):
    _name: str
    _age: Optional[int] = None

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        self._name = new_name

    @property
    def age(self):
        return self._age    
    
    @age.setter
    def age(self, new_age):
        self._age = new_age

    def notify(self, message: str):
        print(f"Notifying {self.name} about -> {message}")
