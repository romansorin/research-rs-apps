import sqlite3
import os

DEFAULT_PATH = os.path.join(os.path.dirname(__file__), 'screenshots.sqlite3')


def db_connect(db_path=DEFAULT_PATH):
    conn = sqlite3.connect(db_path)
    return conn
