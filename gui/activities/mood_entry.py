from datetime import datetime
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPlainTextEdit, QPushButton
from vaaya.gui.models import JrnEntry
from vaaya.utilities import screen_center, NumpyEncoder
from vaaya.emotions import Analyzer
import json


# Have a view previous entries on the main page, that way this can just be an entry
# Known needs:
# Do something with adding to the Application. Idk how this works
# Add CSS styling
# Add code to show on button click (Ok...) button

class MoodEntry(QWidget):
    def __init__(self):
        super().__init__(None, Qt.MSWindowsFixedSizeDialogHint)
        self.setFocusPolicy(Qt.StrongFocus)
        self.setAttribute(Qt.WA_QuitOnClose, True)
        self.setWindowTitle('Describe your day.')
        self.setObjectName('entry-activity')
        self.hbox = QHBoxLayout()
        self.vbox = QVBoxLayout()
        self.entry = QPlainTextEdit()
        self.draw()

    def draw(self):
        view_btn = QPushButton('View Entries')
        view_btn.setObjectName('mood-btn-view')
        view_btn.setProperty('class', 'mood-btn')
        # view_btn.clicked.connect()
        save_btn = QPushButton('Save Entry')
        save_btn.setObjectName('mood-btn-save')
        save_btn.setProperty('class', 'mood-btn')
        save_btn.clicked.connect(self.save_data)
        self.hbox.addWidget(view_btn)
        self.hbox.addStretch()
        self.hbox.addWidget(save_btn)
        self.vbox.addWidget(self.entry)
        self.vbox.addLayout(self.hbox)
        self.setLayout(self.vbox)

    def show(self):
        super().show()
        self.move(screen_center(self))

    @pyqtSlot()
    def open_entries(self):
        # Open the other gui for analytics (maybe just a list of previous entries?)
        pass

    @pyqtSlot()
    def save_data(self):
        user_entry = self.entry.toPlainText()
        analysis = Analyzer(user_entry).analyze()
        jen = JrnEntry(**{
            "log_time": datetime.now(),
            "journal": user_entry,
            "analysis": json.dumps(analysis, cls=NumpyEncoder)
        })
        jen.save()
