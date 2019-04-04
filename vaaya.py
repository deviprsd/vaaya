import sys
import time

from .gui.application import Application, SplashScreen
from .utilities import asset_path
from .gui.activities import MoodActivity
from .contexts import Context
from peewee import SqliteDatabase
import spacy


def run():
    if sys.platform.startswith('win'):
        app = Application(icon=asset_path('logo.jpg'))
    else:
        app = Application(icon=asset_path('vaaya.xbm'))

    with SplashScreen(app, asset_path('logo.jpg'), 2.0) as sp:
        sp.status_update('Loading DataBase and settings ...')
        Context.db = SqliteDatabase('vaaya.db')
        time.sleep(2)
        sp.status_update('Loading module Spacy ...')
        Context.nlp = spacy.load('en_core_web_lg')

    app.setup((MoodActivity,))
    app.mainloop()
