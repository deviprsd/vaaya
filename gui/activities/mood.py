from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton
from ...utilities import asset_path


class MoodActivity(QWidget):
    def __init__(self):
        super().__init__()
        self.grid = QGridLayout()

        self.draw()

    def draw(self):
        smiley = QPushButton('smiley')
        smiley.setIcon(QIcon(asset_path('vaaya_smily.gif')))
        self.grid.addWidget(smiley, 1, 1)

        sad = QPushButton('sad')
        sad.setIcon(QIcon(asset_path('vaaya_sad.gif')))
        self.grid.addWidget(sad, 1, 2)

        angry = QPushButton('angry')
        angry.setIcon(QIcon(asset_path('vaaya_angry.gif')))
        self.grid.addWidget(angry, 1, 3)

        self.setWindowTitle('How are you feeling today?')
        self.setGeometry(100, 100, 500, 500)
        self.setLayout(self.grid)
