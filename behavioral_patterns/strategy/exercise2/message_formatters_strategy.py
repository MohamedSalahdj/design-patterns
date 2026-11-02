from abc import ABC, abstractmethod

from .message import Message
from .format_type import FormatType


class MessageStrategyFormatter(ABC):
    @abstractmethod
    def format(self, msg: Message) -> str: ...

    @abstractmethod
    def get_type(self) -> FormatType: ...