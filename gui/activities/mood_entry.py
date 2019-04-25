from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QBoxLayout, QPlainTextEdit, QPushButton, QLabel
from vaaya.gui.models import DMoods
from vaaya.utilities import asset_path, screen_center

# Have a view previous entries on the main page, that way this can just be an entry

class MoodEntry(QWidget):
    import sys
    from PyQt5.QtCore import *
    from PyQt5.QtGui import *
    from PyQt5.QtWidgets import *

    # Known needs:
    # Do something with adding to the Application. Idk how this works
    # Add CSS styling
    # Add code to show on button click (Ok...) button

    def __init__(self):
        self.window = QWidget()
        self.window.setWindowTitle('Describe your day.')
        self.hbox = QHBoxLayout()
        self.vbox = QVBoxLayout()
        self.entry = QPlainTextEdit(self.window)
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
        self.window.setLayout(self.vbox)

    def show(self):
        # self.window.show() Which one?? Idk
        # super.show()
        self.move(screen_center(self))

    def open_entries(self):
        # Open the other gui for analytics (maybe just a list of previous entries?
        pass

    def save_data(self):
        user_entry = self.entry.toPlainText()
        print(user_entry)
    # Send the data to the data base
    # Have a future method to send the data to previous entry storage
