import sqlite3

CONN = sqlite3.connect('catalogue.db')
CURSOR = CONN.cursor()
