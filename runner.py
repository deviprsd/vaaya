import time
import spacy

from peewee import SqliteDatabase
from PyQt5.QtCore import QFileSystemWatcher
from vaaya.gui.application import Application, SplashScreen
from vaaya.utilities import asset_path, get_icon
from vaaya.contexts import Context
from vaaya.gui.theme import Shraavani


def run():
    app = Application([])
    app.setWindowIcon(get_icon())
    app.setStyleSheet(Shraavani.style_sheet())

    if True:
        def file_changed(path):
            print(path)
            app.setStyleSheet(Shraavani.style_sheet())

        fs_watcher = QFileSystemWatcher([asset_path('qcss/'), asset_path('qcss/shraavani.qcss') ])
        fs_watcher.fileChanged.connect(file_changed)

    with SplashScreen(app, asset_path('logo-splash.jpg')) as sp:
        sp.status_update('Initializing ...')
        Context.app = app
        time.sleep(2)

        sp.status_update('Loading DataBase and settings ...')
        Context.db = SqliteDatabase('vaaya.sqlite')
        Context.db.connect(reuse_if_open=True)
        from vaaya.gui.models import DMoods
        Context.db.create_tables([DMoods])
        time.sleep(2)

        sp.status_update('Loading module Spacy ...')
        try:
            Context.nlp = spacy.load('en_core_web_lg')
        except IOError:
            from spacy.cli import download
            download('en_core_web_lg')
            Context.nlp = spacy.load('en_core_web_lg')

        from vaaya.gui.activities import MoodActivity
        sp.set_after(MoodActivity())

    app.exec_()

