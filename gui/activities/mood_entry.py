from datetime import datetime
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPlainTextEdit, QPushButton, QMessageBox
from vaaya.gui.models import JrnEntry
from vaaya.utilities import screen_center, NumpyEncoder
from vaaya.emotions import Analyzer
import json


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

    # Build the entry gui.
    def draw(self):
        view_btn = QPushButton('View Entries')
        view_btn.setObjectName('mood-btn-ok')
        view_btn.setProperty('class', 'mood-btn')
        view_btn.clicked.connect(self.open_entries)
        save_btn = QPushButton('Save Entry')
        save_btn.setObjectName('mood-btn-ok')
        save_btn.setProperty('class', 'mood-btn')
        save_btn.clicked.connect(self.save_data)
        save_btn.clicked.connect(self.save_success)
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
        self.parent().parent().set_page(1)

    # Save the data to the data base
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

    # Confirm saved
    def save_success(self):
        QMessageBox.about(self, ' ', "Saved Successfully!")