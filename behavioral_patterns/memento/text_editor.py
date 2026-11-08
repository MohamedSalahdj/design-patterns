from dataclasses import dataclass, field


@dataclass
class TextEditor:
    _content: str = ""
    _prev_state: list = field(default_factory=list)
    _next_state: list = field(default_factory=list)

    @property
    def content(self) -> str:
        return self._content

    @content.setter
    def content(self, value: str) -> None:
        self._content = value
    

    def save(self) -> None:
        self._prev_state.append(self._content)
        self._next_state.clear()

    def undo(self) -> str:
        if self._prev_state:                   
            self._next_state.append(self._content)
            self._content = self._prev_state.pop()
            return self._content

    def redo(self) -> None:
        if self._next_state:
            self._prev_state.append(self._content)
            self._content = self._next_state.pop()
            return self._content