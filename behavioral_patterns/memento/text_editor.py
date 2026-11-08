from dataclasses import dataclass

from .text_editor_state import TextEditorState


@dataclass
class TextEditor:
    _content: str = ""

    @property
    def content(self) -> str:
        return self._content

    @content.setter
    def content(self, value: str) -> None:
        self._content = value
    
    def save(self) -> TextEditorState:
        return TextEditorState(self.content)

    def restore(self, text_state: TextEditorState):
        self.content = text_state.content
