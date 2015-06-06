from PyQt4 import QtGui


class MainPresenter:

    def __init__(self, view, model):
        self._item_presenters = []

        self.view = view
        self.view.textbox.returnPressed.connect(self._add_todo)
        self.model = model
        self.model.todo_stream.subscribe(self._update_view)
        self.model.uncompleted_stream\
            .map(lambda items: "{} item{} left".format(
                len(items), "s" if len(items) > 1 else ""))\
            .subscribe(self.view.count_label.setText)
        self.model.todo_stream\
            .map(lambda items: len(items) > 0)\
            .subscribe(self.view.footer.setVisible)

    def _add_todo(self):
        text = self.view.textbox.text().strip()
        if text:
            self.view.textbox.clear()
            self.model.add_todo(text)

    def _update_view(self, todos):
        # Clear layout
        for _ in range(self.view.todo_layout.count()):
            widget = self.view.todo_layout.takeAt(0).widget()
            del widget
        self._item_presenters.clear()

        # Refresh todo widgets
        for todo in todos:
            presenter = TodoItemPresenter(todo)
            self.view.todo_layout.addWidget(presenter.view)
            self._item_presenters.append(presenter)


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

        self.count_label = QtGui.QLabel()

        footer_layout = QtGui.QHBoxLayout()
        footer_layout.addWidget(self.count_label)
        footer_layout.addStretch(1)

        self.footer = QtGui.QWidget()
        self.footer.setLayout(footer_layout)
        self.footer.hide()

        layout = QtGui.QVBoxLayout()
        layout.addWidget(self.textbox)
        layout.addLayout(self.todo_layout)
        layout.addWidget(self.footer)
        layout.addStretch(1)
        self.setLayout(layout)


class TodoItemPresenter:

    def __init__(self, model, view=None):
        self.view = view or TodoItemView()
        self.model = model
        self.model.text_stream.subscribe(self.view.label.setText)
        self.model.completed_stream.subscribe(self.view.check.setChecked)

        self.view.check.clicked.connect(self.model.completed_stream.on_next)


class TodoItemView(QtGui.QWidget):

    def __init__(self):
        super().__init__()
        self.check = QtGui.QCheckBox()
        self.label = QtGui.QLabel()

        layout = QtGui.QHBoxLayout()
        layout.addWidget(self.check)
        layout.addWidget(self.label)
        layout.addStretch(1)
        self.setLayout(layout)
