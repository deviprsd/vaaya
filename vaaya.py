import sys
import time

from .gui.application import Application, SplashScreen
from .utilities import asset_path
from .gui.activities import MoodActivity
from .contexts import Context
from peewee import SqliteDatabase
import spacy


def run():
    app = Application([])
    x = None

    with SplashScreen(app, asset_path('logo-splash.jpg')) as sp:
        x = sp
        sp.status_update('Initializing ...')
        time.sleep(2)
        sp.status_update('Loading DataBase and settings ...')
        Context.db = SqliteDatabase('vaaya.db')
        time.sleep(3)
        sp.status_update('Loading module Spacy ...')
        try:
            Context.nlp = spacy.load('en_core_web_lg')
        except IOError:
            from spacy.cli import download
            download('en_core_web_lg')
            Context.nlp = spacy.load('en_core_web_lg')

    mood = MoodActivity()
    mood.show()
    x.finish(mood)

    sys.exit(app.exec_())
