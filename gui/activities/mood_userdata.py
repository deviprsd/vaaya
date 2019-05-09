import json

import numpy as np
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QLabel

from vaaya.emotions import Confidence
from vaaya.utilities import screen_center
from vaaya.contexts import Context


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
        __emts = ['happy', 'sad', 'angry', 'fear', 'suprise', 'disgusted']
        backbtn = QPushButton(text='Back', parent=self)
        backbtn.setObjectName('mood-btn-ok')
        backbtn.setProperty('class', 'mood-btn-clear')
        backbtn.clicked.connect(self.go_back)
        self.grid.addWidget(backbtn, 0, 2)

        data = Context.cvj
        if not data: return
        data_nlp = Context.nlp(data.journal)
        ja = json.loads(data.analysis)

        confidence = Confidence(data)

        for i, s in enumerate(data_nlp.sents):
            self.grid.addWidget(QLabel(str(s)), i + 1, 0)
            self.grid.addWidget(QLabel(__emts[np.argmax(np.array(ja[i][0]))]), i + 1, 1)
            self.grid.addWidget(QLabel(confidence.confidence_percentage(i)), i + 1, 2)

    def update(self):
        self.clear_grid()
        self.add_data()
        super().update()

    def clear_grid(self):
        while self.grid.count():
            child = self.grid.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

    def go_back(self):
        self.parent().parent().set_page(1)
