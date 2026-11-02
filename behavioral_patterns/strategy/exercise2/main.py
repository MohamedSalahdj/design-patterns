from .format_type import FormatType
from .message import Message
from .message_service import MessageService
from .message_formatters_strategy import MessageStrategyFormatter
from .formatters import JSONMessageFormatter, XMLMessageFormatter, PlainTextMessageFormatter


class MessageFormatterFactory:
    _formatter: dict[FormatType, type[MessageStrategyFormatter]] = {
        FormatType.JSON: JSONMessageFormatter,
        FormatType.XML: XMLMessageFormatter,
        FormatType.PLAIN_TEXT: PlainTextMessageFormatter
    }

    @classmethod
    def create(cls, format_type: FormatType) -> MessageStrategyFormatter:
        try:
            return cls._formatter.get(format_type)()
        except KeyError:
            raise ValueError(f"Unsupported format type: {format_type}")



if __name__ == "__main__":
    message = Message("Salah", "Ziad", "Meeting at 5 < 6 & ready")

    service = MessageService(MessageFormatterFactory.create(format_type=FormatType.JSON))

    for format_type in FormatType:
        service.set_formatter(formatter=MessageFormatterFactory.create(format_type=format_type))
        print(f"--- {service.cuurent_type()} ---")
        print(f"{service.format(message=message)}")
        print("-"*45, "\n")