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

    with SplashScreen(app, asset_path('logo.jpg')) as sp:
        sp.status_update('Loading DataBase and settings ...')
        Context.db = SqliteDatabase('vaaya.db')
        time.sleep(2)
        sp.status_update('Loading module Spacy ...')
        try:
            Context.nlp = spacy.load('en_core_web_lg')
        except IOError:
            from spacy.cli import download
            download('en_core_web_lg')
            Context.nlp = spacy.load('en_core_web_lg')

    app.exec_()
