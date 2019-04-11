from PyQt5.QtWidgets import QApplication, QPushButton


class Button(QPushButton):
    def __init__(self, *args, **kwargs):
        QPushButton.__init__(self, *args, **kwargs)
        self.setAutoRepeat(True)
        self.setAutoRepeatDelay(1000)
        self.setAutoRepeatInterval(1000)
        self.clicked.connect(self.handleClicked)
        self._state = 0

    def handleClicked(self):
        if self.isDown():
            if self._state == 0:
                self._state = 1
                self.setAutoRepeatInterval(50)
                print('press')
            else:
                print('repeat')
        elif self._state == 1:
            self._state = 0
            self.setAutoRepeatInterval(1000)
            print('release')
        else:
            print('click')


if __name__ == '__main__':

    import sys
    app = QApplication(sys.argv)
    button = Button('Test Button')
    button.show()
    sys.exit(app.exec_())