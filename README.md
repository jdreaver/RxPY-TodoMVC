# RxPY TodoMVC

This is an implementation of the popular [TodoMVC](http://todomvc.com/)
application using [RxPY](https://github.com/ReactiveX/RxPY) and PyQt4. This
application also uses the
[Model-View-Presenter (MVP) pattern](http://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93presenter).


# Why?

TodoMVC is a project that implements a todo list using various Javascript MVC
frameworks. This helps developers decide what framework to use for a project
because they can see how the same functionality is implemented in different
ways.

The point of RxPY TodoMVC is much simpler: I wanted to create a small
application to demonstrate the usefulness of RxPY for a desktop GUI
application. RxPY is the official Python implementation of
[ReactiveX](http://reactivex.io/). It offers a nice, clean way to structure
applications that are generally asynchronous or callback-based. In particular,
RxPY facilitates simple presenter logic when hooking up models to views.

Lastly, I wanted to get better at using RxPY, and I figured I could help others
along the way. Before I use RxPY in my more serious projects, I wanted to sort
out exactly how I should structure an MVP app with rx, and integrate with Qt.


# Requirements

* Python 3
* RxPY
* PyQt4

To run, simply execute `python run.py`.


# TODO

Funny how a todo app still has a todo list?

- Finish TodoMVC spec. See the
  [spec here](https://github.com/tastejs/todomvc/blob/master/app-spec.md)
  - Add a combobox to filter by All, Active, and Completed
  - Add a "Clear Completed" button
  - Double click to edit a todo
  - Hide footer if no todos
  - Have a button that marks all todos as complete
- Add tests
- Make the app less imperative and more reactive. There is a lot of callback
  logic still.
  - Better rx logic for uncompleted and completed streams, instead of using a
    callback function to generate them.
- Make everything look pretty. (Should we use QML and PyQt5?)
