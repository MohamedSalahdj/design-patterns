from dataclasses import dataclass


@dataclass
class User:
    _name: str
    _email: str = None
    _mobile_number: str = None

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        self._name = new_name

    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, new_email):
        self._email = new_email

    @property
    def mobile_number(self):
        return self._mobile_number
    
    @mobile_number.setter
    def mobile_number(self, new_mobile_number):
        self._mobile_number = new_mobile_number