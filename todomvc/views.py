from PyQt4 import QtGui


class MainPresenter:

    def __init__(self, view, model):
        self.view = view
        self.view.textbox.returnPressed.connect(self._add_todo)
        self.model = model
        self.model.todo_stream.subscribe(self._update_view)

    def _add_todo(self):
        text = self.view.textbox.text()
        if text:
            self.view.textbox.clear()
            self.model.add_todo(text)

    def _update_view(self, todos):
        # Clear layout
        for _ in range(self.view.todo_layout.count()):
            widget = self.view.todo_layout.takeAt(0).widget()
            del widget

        # Refresh todo widgets
        for todo in todos:
            todo_item_view = TodoItemView(todo.text, todo.completed)
            self.view.todo_layout.addWidget(todo_item_view)


class MainView(QtGui.QWidget):

    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle("RxPY TodoMVC")

        # Used to enter text for a new todo list item
        self.textbox = QtGui.QLineEdit()

        # Holds individual widgets for each todo item
        self.todo_layout = QtGui.QVBoxLayout()

        layout = QtGui.QVBoxLayout()
        layout.addWidget(self.textbox)
        layout.addLayout(self.todo_layout)
        self.setLayout(layout)


class TodoItemView(QtGui.QWidget):

    def __init__(self, text, completed):
        super().__init__()
        self.check = QtGui.QCheckBox()
        self.check.setChecked(completed)
        self.label = QtGui.QLabel(text)

        layout = QtGui.QHBoxLayout()
        layout.addWidget(self.check)
        layout.addWidget(self.label)
        self.setLayout(layout)
