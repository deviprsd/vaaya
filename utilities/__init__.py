import os


def asset_path(file):
    return os.path.abspath(os.path.dirname(__file__) + '/../assets/' + file)
