from PyQt4 import QtGui
import sys

import todomvc


def main():
    app = QtGui.QApplication(sys.argv)

    model = todomvc.TodoListModel()
    view = todomvc.MainView()
    view.show()

    presenter = todomvc.MainPresenter(view, model)

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
