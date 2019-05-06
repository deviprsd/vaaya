from PyQt5.QtGui import QColor, QPixmap
from PyQt5.QtWidgets import QApplication, QSplashScreen, QMainWindow
from PyQt5.QtCore import Qt


# Generate the splash screen
class SplashScreen:
    def __init__(self, parent, image=None, after=None):
        self.app = parent
        image = QPixmap(image)
        image = image.scaled(500, 500, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.splash = QSplashScreen(image, Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.splash.setMask(image.mask())
        self.after = after

    def set_after(self, after):
        self.after = after

    def __enter__(self):
        self.splash.show()
        self.app.processEvents()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.after.show()
        self.splash.finish(self.after)

    def status_update(self, msg):
        self.splash.showMessage(msg, alignment=Qt.AlignHCenter, color=QColor(235, 239, 242))
        self.app.processEvents()


class Application(QApplication):
    pass
