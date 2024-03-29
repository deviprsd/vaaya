from datetime import datetime
from functools import partial

from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QLabel
from vaaya.utilities import asset_path, screen_center
from vaaya.gui.models import DMoods
from vaaya.gui.activities.mood_entry import MoodEntry


class MoodActivity(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.grid = QGridLayout(self)
        self.setObjectName('mood-activity')
        self.draw()

    def draw(self):
        """
        Function that create emotion visual
        :return:
        """
        self.__add_btns(['smiley', 'sad', 'angry', 'disgusted', 'fear', 'surprised'])
        self.setWindowTitle('How are you feeling today?')
        self.setLayout(self.grid)
        self.setGeometry(0, 0, 450, 200)

    def show(self):
        super().show()
        self.move(screen_center(self))

    def __add_btns(self, btns_info):
        """
        Creates ok, clear and mood buttons
        sets button labels
        Updates percentages on button click
        :param btns_info:
        :return:
        """
        lbls, btns = [], []
        for i, md in enumerate(btns_info):
            btn = QPushButton(text='', parent=self)
            btns.append(btn)
            btn.setIcon(QIcon(asset_path('vaaya_{}.gif'.format(md))))
            btn.setObjectName('mood-btn-{}'.format(md))
            btn.setProperty('class', 'mood-btn')
            btn.setAutoRepeat(True)
            btn.setAutoRepeatDelay(500)
            btn.setAutoRepeatInterval(50)

            label = QLabel('0%', parent=self)
            lbls.append(label)
            label.setAlignment(Qt.AlignCenter)
            label.setObjectName('mood-label-{}'.format(md))
            label.setProperty('class', 'mood-label')

            # Update the percentages on button click
            btn.clicked.connect(partial(self.mood, btn, label))
            self.grid.addWidget(btn, 1, i + 1)
            self.grid.addWidget(label, 2, i + 1)

        # Make ok and clear buttons
        ok_btn = QPushButton('OK ...', self)
        ok_btn.setAutoDefault(True)
        ok_btn.setObjectName('mood-btn-ok')
        ok_btn.setProperty('class', 'mood-btn')

        clear_btn = QPushButton('Clear ...', self)
        clear_btn.setObjectName('mood-btn-ok')
        clear_btn.setProperty('class', 'mood-btn')

        self.grid.addWidget(ok_btn, 3, len(btns_info))
        self.grid.addWidget(clear_btn, 3, 1)

        clear_btn.clicked.connect(partial(self.clear, lbls))
        ok_btn.clicked.connect(partial(self.save_mood_data, lbls))
        ok_btn.clicked.connect(self.open_entry)

    @pyqtSlot()
    def clear(self, labels):
        """
        Clears labels
        Used for deleting entries
        :param labels:
        :return:
        """
        for lbl in labels:
            lbl.setText('0%')

    @pyqtSlot()
    def mood(self, btn, label):
        """
        Sets label to appropriate mood
        :param btn:
        :param label:
        :return:
        """
        label.setText('{}%'.format(min(int(label.text().strip('%')) + 1, 100)))

    @pyqtSlot()
    def open_entry(self):
        """
        Opens diary entry from entries page
        :return:
        """
        self.parent().parent().set_page(1)

    @pyqtSlot()
    def save_mood_data(self, labels):
        """
        Sets the log time, saves appropriate mood label
        :param labels:
        :return:
        """
        model_args, lbl, vec = {"log_time": datetime.now()}, None, []
        for lbl in labels:
            vec.append(int(lbl.text().strip('%')))
            model_args[lbl.objectName().split('-')[2]] = int(lbl.text().strip('%'))
        if max(vec) == 0: return
        dms = DMoods(**model_args)
        dms.save()
