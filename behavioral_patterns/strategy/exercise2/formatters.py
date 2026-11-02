import json
import xml.etree.ElementTree as ET
from dataclasses import asdict
from .format_type import FormatType
from .message_formatters_strategy import MessageStrategyFormatter
from .message import Message


class JSONMessageFormatter(MessageStrategyFormatter):
    def format(self, message: Message) -> str:
        return json.dumps(asdict(message), ensure_ascii=False, indent=False)

    def get_type(self) -> FormatType: 
        return FormatType.JSON.name


class XMLMessageFormatter(MessageStrategyFormatter):
    def format(self, message: Message) -> str:
        root = ET.Element("message")
        for field_name, value in asdict(message).items():
            ET.SubElement(root, field_name).text = str(value)
        return ET.tostring(root, encoding="unicode")

    def get_type(self) -> FormatType:
        return FormatType.XML.name


class PlainTextMessageFormatter(MessageStrategyFormatter):
    def format(self, message: Message) -> str:
        return (
            f"From: {message.sender}\n"
            f"To: {message.recipient}\n"
            f"Body: {message.body}"
        )


    def get_type(self) -> FormatType:
        return FormatType.PLAIN_TEXT.name
