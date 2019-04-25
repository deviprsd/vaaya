import time
import spacy

from peewee import SqliteDatabase
from PyQt5.QtCore import QFileSystemWatcher
from vaaya.gui.application import Application, SplashScreen
from vaaya.utilities import asset_path, get_icon
from vaaya.contexts import Context
from vaaya.gui.theme import Shraavani


def run():
    """
    Initialized the program, and it's dependencies, set Context variables required through out the program
    for performance during splashscreen, and then open the first window
    :return: None
    """

    app = Application([])
    app.setWindowIcon(get_icon())
    app.setStyleSheet(Shraavani.style_sheet())

    if True:
        def file_changed(path):
            print(path) # TODO make debugging only in development
            app.setStyleSheet("") # reset for overlapping issues
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
        time.sleep(1)

        sp.status_update('Loading module Spacy ...')
        try:
            Context.nlp = spacy.load('en_core_web_lg')
        except IOError:
            sp.status_update('Downloading Spacy dependencies (est. 826 mb in size)')
            from spacy.cli import download
            download('en_core_web_lg')
            Context.nlp = spacy.load('en_core_web_lg')

        from vaaya.gui.activities import MoodActivity

        # Add mood entry import here (on ok... button click)
        sp.set_after(MoodActivity())

    app.exec_()

