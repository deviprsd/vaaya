from datetime import datetime
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton
from vaaya.gui.models import JrnEntry
from vaaya.utilities import screen_center
from vaaya.contexts import Context
from vaaya.emotions import Analyzer
import json


# Displays the analysis of the text with the confidence factor.
class MoodData(QWidget):
    def __init__(self):
        super().__init__(None, Qt.MSWindowsFixedSizeDialogHint)
        self.setFocusPolicy(Qt.StrongFocus)
        self.setAttribute(Qt.WA_QuitOnClose, True)
        self.grid = QGridLayout()
        self.draw()

    def draw(self):
        self.add_data()
        self.setWindowTitle('Your text analysis')
        self.setLayout(self.grid)
        self.setGeometry(0, 0, 450, 450)

    def show(self):
        super().show()
        self.move(screen_center(self))

    # Fill the GUI
    def add_data(self):
        backbtn = QPushButton(text='Back', parent=self)
        backbtn.setObjectName('mood-btn-ok')
        backbtn.setProperty('class', 'mood-btn-clear')
        backbtn.clicked.connect(self.go_back)
        self.grid.addWidget(backbtn, 0, 1)

        #loc = Context.cvj
        #data = JrnEntry.get(JrnEntry.log_time == loc)

        # loop. to make the columns skinnier use btn.setFixedWidth(size)

    # Go to the previous screen
    def go_back(self):
        self.parent().parent().set_page(1)
