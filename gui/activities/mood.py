from datetime import datetime
from functools import partial

from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QLabel
from vaaya.utilities import asset_path, screen_center
from vaaya.gui.models import DMoods
from vaaya.gui.activities.mood_entry import MoodEntry


class MoodActivity(QWidget):
    def __init__(self):
        super().__init__(None, Qt.MSWindowsFixedSizeDialogHint)
        self.grid = QGridLayout()
        self.setObjectName('mood-activity')
        self.draw()

    def draw(self):
        self.__add_btns(['smiley', 'sad', 'angry', 'disgusted', 'fear', 'surprised'])
        self.setWindowTitle('How are you feeling today?')
        self.setLayout(self.grid)

    def show(self):
        super().show()
        self.move(screen_center(self))

    def __add_btns(self, btns_info):
        lbls, btns = [], []
        for i, md in enumerate(btns_info):
            btn = QPushButton(text='')
            btns.append(btn)
            btn.setIcon(QIcon(asset_path('vaaya_{}.gif'.format(md))))
            btn.setObjectName('mood-btn-{}'.format(md))
            btn.setProperty('class', 'mood-btn')
            btn.setAutoRepeat(True)
            btn.setAutoRepeatDelay(500)
            btn.setAutoRepeatInterval(50)

            label = QLabel('0%')
            lbls.append(label)
            label.setAlignment(Qt.AlignCenter)
            label.setObjectName('mood-label-{}'.format(md))
            label.setProperty('class', 'mood-label')

            # Update the percentages on button click
            btn.clicked.connect(partial(self.mood, btn, label))
            self.grid.addWidget(btn, 1, i + 1)
            self.grid.addWidget(label, 2, i + 1)

        # Make ok and clear buttons
        ok_btn = QPushButton('OK ...')
        ok_btn.setAutoDefault(True)
        ok_btn.setObjectName('mood-btn-ok')
        ok_btn.setProperty('class', 'mood-btn')  # This is how use the css styling for a group of objects

        clear_btn = QPushButton('Clear ...')
        clear_btn.setObjectName('mood-btn-ok')  # Maybe this should be mood-btn (they should look the same?)
        clear_btn.setProperty('class', 'mood-btn')

        self.grid.addWidget(ok_btn, 3, len(btns_info))
        self.grid.addWidget(clear_btn, 3, 1)

        clear_btn.clicked.connect(partial(self.clear, lbls))
        ok_btn.clicked.connect(partial(self.save_mood_data, lbls))
        ok_btn.clicked.connect(self.open_entry)

    @pyqtSlot()
    def clear(self, labels):
        for lbl in labels:
            lbl.setText('0%')

    @pyqtSlot()
    def mood(self, btn, label):
        label.setText('{}%'.format(min(int(label.text().strip('%')) + 1, 100)))

    @pyqtSlot()
    def open_entry(self):
        m = MoodEntry()
        m.show()

    @pyqtSlot()
    def save_mood_data(self, labels):
        model_args, lbl = {"log_time": datetime.now()}, None
        for lbl in labels:
            model_args[lbl.objectName().split('-')[2]] = int(lbl.text().strip('%'))

        dms = DMoods(**model_args)
        dms.save()
