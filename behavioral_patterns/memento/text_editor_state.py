from dataclasses import dataclass


@dataclass(frozen=True)
class TextEditorState:
    content: str
