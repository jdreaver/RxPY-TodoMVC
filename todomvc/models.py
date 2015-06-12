from collections import namedtuple
import rx


TodoItem = namedtuple("TodoItem", ["text", "completed"])


class TodoListModel:

    def __init__(self):
        self._todos = []  # List of strings
        self.todo_stream = rx.subjects.BehaviorSubject(self._todos)
        self.completed_stream = rx.subjects.BehaviorSubject([])
        self.uncompleted_stream = rx.subjects.BehaviorSubject([])

    def _publish(self):
        self.todo_stream.on_next(self._todos)
        self._publish_completed()

    def _publish_completed(self, *args):
        self.completed_stream.on_next(
            [t for t in self._todos if t.completed])
        self.uncompleted_stream.on_next(
            [t for t in self._todos if not t.completed])

    def add_todo(self, text):
        item = TodoItem(self, text)
        item.completed_stream.subscribe(self._publish_completed)
        self._todos.append(item)
        self._publish()

    def remove_todo(self, todo_item):
        self._todos.remove(todo_item)
        self._publish()


class TodoItem:

    def __init__(self, parent, text, completed=False):
        self.parent = parent

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

    def delete(self):
        self.parent.remove_todo(self)

    def __repr__(self):
        return "<TodoItem(text={}, completed={})>".format(
            self.text, self.completed)
