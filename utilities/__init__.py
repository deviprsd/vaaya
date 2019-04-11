def asset_path(file):
    import os
    return os.path.abspath(os.path.dirname(__file__) + '/../assets/' + file)


def get_icon():
    from PyQt5.QtGui import QIcon
    from PyQt5.QtCore import QSize
    app_icon = QIcon()
    app_icon.addFile(asset_path('/icons/icon16.png'), QSize(16, 16))
    app_icon.addFile(asset_path('/icons/icon24.png'), QSize(24, 24))
    app_icon.addFile(asset_path('/icons/icon32.png'), QSize(32, 32))
    app_icon.addFile(asset_path('/icons/icon48.png'), QSize(48, 48))
    app_icon.addFile(asset_path('/icons/icon64.png'), QSize(64, 64))
    app_icon.addFile(asset_path('/icons/icon256.png'), QSize(256, 256))
    return app_icon


def screen_center(widget):
    from PyQt5.QtWidgets import QApplication
    return QApplication.desktop().screen().rect().center()- widget.rect().center()

