from datetime import datetime
from functools import partial
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.QtWidgets import QWidget, QGridLayout, QVBoxLayout, QHBoxLayout, QMessageBox, QPushButton
from vaaya.gui.models import JrnEntry
from vaaya.utilities import screen_center, NumpyEncoder
from vaaya.emotions import Analyzer
import json


class MoodAnalytics(QWidget):
    def __init__(self):  # Need to take in DB as parameter?
        super().__init__(None, Qt.MSWindowsFixedSizeDialogHint)
        self.setFocusPolicy(Qt.StrongFocus)
        self.setAttribute(Qt.WA_QuitOnClose, True)
        self.setWindowTitle('Previous entries and data.')
        self.grid = QGridLayout(self)
        self.draw()

    def draw(self):
        self.add_entries()
        self.setWindowTitle('Previous entries and data')
        self.setLayout(self.grid)
        self.setGeometry(0, 0, 450, 200)

    def show(self):
        super().show()
        self.move(screen_center(self))

    def add_entries(self):
        btns = []
        for i, entry in enumerate(JrnEntry.select()):
            btn = QPushButton(text='Journal' + str(i) + ': ' + str(entry.log_time), parent=self)
            btns.append(btn)
            btn.setObjectName('mood-btn-ok')
            btn.setProperty('class', 'mood-btn')
            btn.connect.partial(self.show_data, entry.log_time)
            self.grid.addWidget(btn, i, 0)

            # Build buttons
            # add the buttons to grid
            # add message box popup
        # Do data base stuff here. Not sure how it works entirely
        # for entry in database entries:
        #

    def show_entries(self, date):
        data = JrnEntry.get(JrnEntry.log_time == date)
        # Data now has the entry stuff
