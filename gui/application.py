from PyQt5.QtGui import QColor, QPixmap
from PyQt5.QtWidgets import QApplication, QSplashScreen, QMainWindow
from PyQt5.QtCore import Qt
from .activities import MoodActivity
from .theme import Shraavani, Colors


class SplashScreen(QSplashScreen):
    def __init__(self, parent, image=None):
        self.app = parent
        image = QPixmap(image)
        image = image.scaled(500, 500, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        super().__init__(image, Qt.FramelessWindowHint)
        self.setMask(image.mask())

    def __enter__(self):
        self.show()
        self.app.processEvents()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        #self.finish(start_activity)
        pass

    def status_update(self, msg):
        self.showMessage(msg, alignment=Qt.AlignHCenter, color=QColor(235, 239, 242))
        self.app.processEvents()


class Application(QApplication):
    pass
