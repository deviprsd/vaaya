from zipfile import ZipFile
from pathlib import Path
from vaaya.utilities import asset_path


def extract_zips(directory):
    zip_files = list(Path(asset_path(directory)).rglob("*.[zZ][iI][pP]"))
    for zipf in zip_files:
        with ZipFile(zipf) as zip:
            zip.extractall(asset_path('corpus'))


def remove_unwanted():
    pass


def lemmatize():
    pass