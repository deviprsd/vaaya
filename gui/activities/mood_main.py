from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QStackedWidget, QHBoxLayout, QWidget, QVBoxLayout
from utilities import screen_center
from vaaya.gui.activities import MoodActivity, MoodAnalytics


class MoodStackedActivity(QWidget):
    def __init__(self, widgets, main):
        super().__init__()
        self.widgets = widgets
        self.win = main
        self.stacker = QStackedWidget(self)

        for w in self.widgets:
            self.stacker.addWidget(w)

        self.v_layout = QVBoxLayout()
        self.v_layout.addWidget(QWidget())
        self.v_layout.addWidget(self.stacker)

        self.setLayout(self.v_layout)

        self.set_page(0)

    def show(self):
        super().show()
        self.move(screen_center(self))

    def windowTitle(self):
        return self.widgets[self.stacker.currentIndex()].windowTitle()

    def set_page(self, i):
        if not i < len(self.widgets): return
        self.win.setWindowTitle(self.widgets[i].windowTitle())
        self.stacker.setCurrentIndex(i)


class MoodMainActivity(QMainWindow):
    def __init__(self, widgets):
        super().__init__(None, Qt.MSWindowsFixedSizeDialogHint)
        self.stacker = QStackedWidget(self)
        self.stacker.setProperty('class', 'ctm-widget')
        self.widgets = [MoodActivity(self), MoodStackedActivity(widgets, self)]

        for w in self.widgets:
            self.stacker.addWidget(w)

        self.c_layout = QHBoxLayout()
        self.c_layout.addWidget(self.stacker)

        self.setLayout(self.c_layout)
        self.set_page(0)

    def show(self):
        super().show()
        self.move(screen_center(self))

    def set_page(self, i):
        self.setWindowTitle(self.widgets[i].windowTitle())
        self.stacker.setGeometry(self.widgets[i].geometry())
        self.setGeometry(self.widgets[i].geometry())
        self.stacker.setCurrentIndex(i)
        self.move(screen_center(self))
