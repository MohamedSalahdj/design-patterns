from dataclasses import dataclass, field

from .text_editor_state import TextEditorState


@dataclass
class History:
    _prev_state: list = field(default_factory=list)
    _next_state: list = field(default_factory=list)

    def save_history_state(self, text_editor_state: TextEditorState):
        self._prev_state.append(text_editor_state)
        self._next_state.clear()

    def undo(self):
        if len(self._prev_state) > 1:
            self._next_state.append(self._prev_state.pop())
            return self._prev_state[-1]
        return None

    def redo(self):
        if self._next_state:
            self._prev_state.append(self._next_state.pop())
            return self._prev_state[-1]
        return None
