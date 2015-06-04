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


class TodoItem:

    def __init__(self, text, completed=False):
        # A BehaviorSubject caches the latest emitted value, and this value is
        # immediately emitted when a new observer subscribes.
        self.text_stream = rx.subjects.BehaviorSubject(text)
        self.completed_stream = rx.subjects.BehaviorSubject(completed)

    @property
    def text(self):
        return self.text_stream.value

    @text.setter
    def text(self, value):
        self.text_stream.on_next(value)

    @property
    def completed(self):
        return self.completed_stream.value

    @completed.setter
    def completed(self, value):
        self.completed.on_next(value)

    def __repr__(self):
        return "<TodoItem(text={}, completed={})>".format(
            self.text, self.completed)
