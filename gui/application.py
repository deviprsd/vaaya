import sys
import time

from PyQt5.QtGui import QColor, QPixmap
from PyQt5.QtWidgets import QApplication, QSplashScreen
from PyQt5.QtCore import Qt
from .activities import MoodActivity
from .theme import Shraavani, Colors


class SplashScreen(QSplashScreen):
    def __init__(self, parent, image=None):
        self.app = parent
        image = QPixmap(image)
        image = image.copy(0, 250, image.width(), image.height() - 500)
        image = image.scaled(400, 400, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        super().__init__(image, Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)

    def __enter__(self):
        self.show()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        # self.finish(MoodActivity)
        pass

    def status_update(self, msg):
        self.showMessage(msg, alignment=Qt.AlignHCenter, color=QColor())
        self.app.processEvents()


class Application(QApplication):
    pass
