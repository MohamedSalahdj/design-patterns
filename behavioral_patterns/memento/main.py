from .text_editor import TextEditor
from .history import History
from .text_editor_state import TextEditorState

if __name__ == "__main__":
    editor = TextEditor()
    history = History()

    editor.content = "Hello, "
    history.save_history_state(editor.save())

    editor.content = "World!"
    history.save_history_state(editor.save())

    editor.content = "Welcome to the Memento Pattern."
    history.save_history_state(editor.save())

    editor.content = "This is a text editor."

    editor.restore(history.undo())

    print(f"Current content after undo: {editor.content}")