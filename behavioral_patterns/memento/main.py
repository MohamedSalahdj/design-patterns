from .text_editor import TextEditor

if __name__ == "__main__":
    editor = TextEditor()
    editor.content = "Hello, "
    editor.save()

    editor.content = "World!"
    editor.save()

    editor.content = "Welcome to the Memento pattern."

    editor.undo()
    editor.undo()
    print(editor.content)
    
    editor.redo()
    print(editor.content) 

    editor.redo()
    print(editor.content)