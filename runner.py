import time
import spacy

from peewee import SqliteDatabase
from vaaya.gui.application import Application, SplashScreen
from vaaya.utilities import asset_path, get_icon
from vaaya.contexts import Context
from vaaya.gui.theme import Shraavani


def run():
    app = Application([])
    app.setWindowIcon(get_icon())
    app.setStyleSheet(Shraavani.style_sheet)

    with SplashScreen(app, asset_path('logo-splash.jpg')) as sp:
        sp.status_update('Initializing ...')
        Context.set_app(app)
        time.sleep(2)
        sp.status_update('Loading DataBase and settings ...')
        Context.set_db(SqliteDatabase('vaaya.sqlite'))
        Context.get_db().connect(reuse_if_open=True)
        from vaaya.gui.models import DMoods
        Context.get_db().create_tables([DMoods], safe=False)
        time.sleep(3)
        sp.status_update('Loading module Spacy ...')
        try:
            Context.set_nlp(spacy.load('en_core_web_lg'))
        except IOError:
            from spacy.cli import download
            download('en_core_web_lg')
            Context.set_nlp(spacy.load('en_core_web_lg'))

        from vaaya.gui.activities import MoodActivity
        sp.set_after(MoodActivity())

    app.exec_()

