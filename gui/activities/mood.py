from datetime import datetime
from functools import partial

from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QLabel
from vaaya.utilities import asset_path, screen_center
from vaaya.gui.models import DMoods


class MoodActivity(QWidget):
    def __init__(self):
        super().__init__(None, Qt.MSWindowsFixedSizeDialogHint)
        self.grid = QGridLayout()
        self.setObjectName('')
        self.draw()

    def draw(self):
        self.__add_btns(['smiley', 'sad', 'angry', 'disgusted', 'fear', 'surprised'])
        self.setWindowTitle('How are you feeling today?')
        self.setLayout(self.grid)

    def show(self):
        super().show()
        self.move(screen_center(self))

    def __add_btns(self, btns_info):
        for i, md in enumerate(btns_info):
            btn = QPushButton(' {}'.format(md.title()))
            btn.setIcon(QIcon(asset_path('vaaya_{}.gif'.format(md))))
            btn.setObjectName('mood-btn')
            btn.setAutoRepeat(True)
            btn.setAutoRepeatDelay(500)
            btn.setAutoRepeatInterval(50)

            label = QLabel('0%')
            label.setAlignment(Qt.AlignCenter)
            label.setObjectName('mood-label-{}'.format(md.title()))

            btn.clicked.connect(partial(self.mood, btn, label))
            self.grid.addWidget(btn, 1, i + 1)
            self.grid.addWidget(label, 2, i + 1)

        ok_btn = QPushButton('OK ...')
        ok_btn.setAutoDefault(True)
        self.grid.addWidget(ok_btn, 3, len(btns_info))
        ok_btn.clicked.connect(self.save_mood_data)

    @pyqtSlot()
    def mood(self, btn, label):
        label.setText('{}%'.format(int(label.text().strip('%')) + 1))

    @pyqtSlot()
    def save_mood_data(self):
        model_args, lbl = {"log_time": datetime.now()}, None
        for i in range(self.grid.count()):
            lbl = self.grid.itemAt(i).widget()
            if isinstance(lbl, QLabel):
                model_args[lbl.objectName()[lbl.objectName().rindex('-'):].lower()] = int(lbl.text().strip('%'))

        dms = DMoods(**model_args)
        dms.save()
