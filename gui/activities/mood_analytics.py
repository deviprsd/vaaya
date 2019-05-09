from functools import partial

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton

from vaaya.contexts import Context
from vaaya.gui.models import JrnEntry
from vaaya.utilities import screen_center


# UPDATE DEVI:
# Get CSS on buttons (fix trim)
# Add scroll bar
# get delete functioning (refresh the screen)
# add ml data. Format this with the moods and text entry
# Add comments

class MoodAnalytics(QWidget):
    def __init__(self):  # Need to take in DB as parameter?
        super().__init__(None, Qt.MSWindowsFixedSizeDialogHint)
        self.setFocusPolicy(Qt.StrongFocus)
        self.setAttribute(Qt.WA_QuitOnClose, True)
        self.grid = QGridLayout(self) # self
        self.draw()

    def draw(self):
        self.add_entries()
        self.setWindowTitle('Click an Entry')
        self.setLayout(self.grid) # self.grid
        self.setGeometry(0, 0, 450, 200)

    def show(self):
        super().show()
        self.move(screen_center(self))

    def add_entries(self):
        backbtn = QPushButton(text='Back', parent=self)
        backbtn.setObjectName('mood-btn-ok')
        backbtn.setProperty('class', 'mood-btn-clear')
        backbtn.clicked.connect(self.go_back)
        clearbtn = QPushButton(text='Delete All Previous Entries', parent=self)
        clearbtn.setObjectName('mood-btn-ok')
        clearbtn.setProperty('class', 'mood-btn-clear')
        clearbtn.clicked.connect(self.delete_all_entries)
        self.grid.addWidget(backbtn, 0, 1)
        self.grid.addWidget(clearbtn, 0, 0)

        for i, entry in enumerate(JrnEntry.select()):
            btn = QPushButton(text='Journal ' + str(i + 1) + ': ' + str(entry.log_time), parent=self)
            btn.setObjectName('mood-btn-ok')
            btn.setProperty('class', 'mood-btn')
            btn.clicked.connect(partial(self.show_entries, entry.log_time))
            dltbtn = QPushButton(text='Delete', parent=self)
            dltbtn.setFixedWidth(50)
            dltbtn.setObjectName('mood-btn-ok')
            dltbtn.setProperty('class', 'mood-btn')
            dltbtn.clicked.connect(partial(self.delete_entry, entry.log_time))
            self.grid.addWidget(btn, i + 1, 0)
            self.grid.addWidget(dltbtn, i + 1, 1)

    def show_entries(self, date):
        data = JrnEntry.get(JrnEntry.log_time == date)
        Context.cvj = data
        self.parent().parent().set_page(2)
        # QMessageBox.about(self, 'Journal Entry Data', data.journal)
        # ADD ML DATA HERE

    def delete_entry(self, date):
        data = JrnEntry.get(JrnEntry.log_time == date)
        data.delete_instance()
        self.update()

    def update(self):
        self.clear_grid()
        self.add_entries()
        super().update()

    def clear_grid(self):
        while self.grid.count():
            child = self.grid.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

    def go_back(self):
        self.parent().parent().set_page(0)

    def delete_all_entries(self):
        JrnEntry.delete().execute()
        self.clear_grid()
        self.add_entries()
        super().update()
