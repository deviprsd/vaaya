import sys

from .gui.application import Application, SplashScreen
from .utilities import asset_path
from .gui.activities import MoodActivity


def run():
    if sys.platform.startswith('win'):
        app = Application(icon=asset_path('logo.jpg'))
    else:
        app = Application(icon=asset_path('vaaya.xbm'))

    with SplashScreen(app, asset_path('logo.jpg'), 3.0):
        pass
    app.setup((MoodActivity,))
    app.mainloop()
