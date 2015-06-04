from collections import namedtuple
import rx


TodoItem = namedtuple("TodoItem", ["text", "completed"])


class TodoListModel:

    def __init__(self):
        self._todos = []  # List of strings
        self.todo_stream = rx.subjects.Subject()

    def _publish(self):
        self.todo_stream.on_next(self._todos)

    def add_todo(self, text):
        self._todos.append(TodoItem(text))
        self._publish()

    def remove_todo(self, index):
        self._todos.pop(index)
        self._publish()

    def toggle_completed(self, index):
        self._todos[index].completed = not self._todos[index].completed
        self._publish()


class TodoItem:

    def __init__(self, text, completed=False):
        self.text = text
        self.completed = completed

    def __repr__(self):
        return "<TodoItem(text={}, completed={})>".format(
            self.text, self.completed)
