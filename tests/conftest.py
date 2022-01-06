import random
import sqlite3

import pytest

from settings import *


def pytest_assertrepr_compare(op, left, right):
    if "ship" in left[0].lower():
        return [f"{left[0]}, " + ", ".join([i for i, j in zip(left, right) if i != j])] + \
               [f"\texpected {i}, was {j}" for i, j in zip(left, right) if i != j]
    else:
        return [f"{left[-1]}, {left[0]}"] + \
               [f"\texpected {i}, was {j}" for i, j in zip(left, right) if i != j]


@pytest.fixture(scope="session")
def storage_database():
    return sqlite3.connect(DATABASE_PATH)


@pytest.fixture(scope="session")
def randomized_database():
    m_db = sqlite3.connect(":memory:")
    s_db = sqlite3.connect(DATABASE_PATH)
    s_db.backup(m_db)
    s_db.close()

    cursor = m_db.cursor()
    ships = [i[0] for i in cursor.execute("SELECT ship FROM Ships").fetchall()]
    for ship in ships:
        ship = cursor.execute(f"SELECT * FROM Ships WHERE ship = '{ship}'").fetchone()
        if random.random() <= 0.33:
            cursor.execute(f"UPDATE Ships SET weapon = 'Weapon_{random.randint(1, w_count)}' WHERE ship = '{ship[0]}'")
        elif random.random() <= 0.5:
            cursor.execute(f"UPDATE Ships SET hull = 'Hull_{random.randint(1, h_count)}' WHERE ship = '{ship[0]}'")
        else:
            cursor.execute(f"UPDATE Ships SET engine = 'Engine_{random.randint(1, e_count)}' WHERE ship = '{ship[0]}'")

    weapons = [i[0] for i in cursor.execute("SELECT weapon FROM Weapons").fetchall()]
    for weapon in weapons:
        weapon = cursor.execute(f"SELECT * FROM Weapons WHERE weapon = '{weapon}'").fetchone()
        if random.random() <= 0.33:
            cursor.execute(f"UPDATE Weapons SET reload_speed = {random.randint(1, 20)} WHERE weapon = '{weapon[0]}'")
        elif random.random() <= 0.5:
            cursor.execute(f"UPDATE Weapons SET rotation_speed = {random.randint(1, 20)} WHERE weapon = '{weapon[0]}'")
        elif random.random() <= 0.5:
            cursor.execute(f"UPDATE Weapons SET diameter = {random.randint(1, 20)} WHERE weapon = '{weapon[0]}'")
        elif random.random() <= 0.5:
            cursor.execute(f"UPDATE Weapons SET power_volley = {random.randint(1, 20)} WHERE weapon = '{weapon[0]}'")
        else:
            cursor.execute(f"UPDATE Weapons SET count = {random.randint(1, 20)} WHERE weapon = '{weapon[0]}'")
    m_db.commit()
    return m_db
