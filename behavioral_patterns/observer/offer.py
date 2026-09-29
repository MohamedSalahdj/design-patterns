from dataclasses import dataclass


@dataclass
class Offer:
    _message : str

    @property
    def message(self):
        return self._message

    @message.setter
    def message(self, new_message: str):
        self._message = new_message