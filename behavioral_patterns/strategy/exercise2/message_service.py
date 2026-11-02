from .format_type import FormatType
from .message import Message
from .message_formatters_strategy import MessageStrategyFormatter


class MessageService:
    def __init__(self, formatter: MessageStrategyFormatter):
        self._formatter = formatter

    def set_formatter(self, formatter: MessageStrategyFormatter) -> None:
        self._formatter = formatter

    def cuurent_type(self) -> FormatType:
        return self._formatter.get_type()

    def format(self, message: Message) -> str:
        return self._formatter.format(message=message)