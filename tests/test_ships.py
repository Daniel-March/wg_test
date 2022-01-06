import sqlite3

import pytest

import settings

db = sqlite3.connect(settings.DATABASE_PATH)
cursor = db.cursor()
ships = cursor.execute("SELECT * FROM Ships").fetchall()
cursor.close()
db.close()


@pytest.mark.parametrize("ship", ships)
def test_weapons(ship, randomized_database: sqlite3.Connection, storage_database: sqlite3.Connection):
    r_cursor = randomized_database.cursor()
    s_cursor = storage_database.cursor()
    r_ship = r_cursor.execute(f"SELECT * FROM Ships WHERE ship = '{ship[0]}'").fetchone()
    assert ship == r_ship

    weapon = list(s_cursor.execute(f"SELECT * FROM Weapons WHERE weapon = '{ship[1]}'").fetchone()) + [ship[0]]
    r_weapon = list(r_cursor.execute(f"SELECT * FROM Weapons WHERE weapon = '{ship[1]}'").fetchone()) + [ship[0]]
    assert weapon == r_weapon


@pytest.mark.parametrize("ship", ships)
def test_hulls(ship, randomized_database: sqlite3.Connection, storage_database: sqlite3.Connection):
    r_cursor = randomized_database.cursor()
    s_cursor = storage_database.cursor()
    r_ship = r_cursor.execute(f"SELECT * FROM Ships WHERE ship = '{ship[0]}'").fetchone()
    assert ship == r_ship

    hull = list(s_cursor.execute(f"SELECT * FROM Hulls WHERE hull = '{ship[2]}'").fetchone()) + [ship[0]]
    r_hull = list(r_cursor.execute(f"SELECT * FROM Hulls WHERE hull = '{ship[2]}'").fetchone()) + [ship[0]]
    assert hull == r_hull


@pytest.mark.parametrize("ship", ships)
def test_engines(ship, randomized_database: sqlite3.Connection, storage_database: sqlite3.Connection):
    r_cursor = randomized_database.cursor()
    s_cursor = storage_database.cursor()
    r_ship = r_cursor.execute(f"SELECT * FROM Ships WHERE ship = '{ship[0]}'").fetchone()
    assert ship == r_ship

    engine = list(s_cursor.execute(f"SELECT * FROM Engines WHERE engine = '{ship[3]}'").fetchone()) + [ship[0]]
    r_engine = list(r_cursor.execute(f"SELECT * FROM Engines WHERE engine = '{ship[3]}'").fetchone()) + [ship[0]]
    assert engine == r_engine
