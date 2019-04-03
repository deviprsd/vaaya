import sys

from .gui.application import Application, SplashScreen
from .utilities import asset_path


def run():
    if sys.platform.startswith('win'):
        app = Application(icon=asset_path('logo.jpg'))
    else:
        app = Application(icon=asset_path('vaaya.xbm'))

    with SplashScreen(app, asset_path('logo.jpg'), 3.0):
        pass  # loading database and stuff
    app.mainloop()
