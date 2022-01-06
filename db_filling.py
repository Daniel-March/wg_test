import sqlite3
from random import randint

import settings


def _r():
    return randint(1, 20)


db = sqlite3.connect(settings.DATABASE_PATH)
cursor = db.cursor()

for i in range(settings.w_count):
    cursor.execute(f"INSERT INTO Weapons VALUES ('Weapon_{i}', {_r()}, {_r()}, {_r()}, {_r()}, {_r()})")

for i in range(settings.h_count):
    cursor.execute(f"INSERT INTO Hulls VALUES ('Hull_{i}', {_r()}, {_r()}, {_r()})")

for i in range(settings.e_count):
    cursor.execute(f"INSERT INTO Engines VALUES ('Engines_{i}', {_r()}, {_r()})")

for i in range(settings.s_count):
    w = randint(0, settings.w_count - 1)
    h = randint(0, settings.h_count - 1)
    e = randint(0, settings.e_count - 1)
    cursor.execute(f"INSERT INTO Ships VALUES ('Ship_{i}', 'Weapon_{w}', 'Hull_{h}','Engines_{e}')")

cursor.close()
db.commit()
db.close()