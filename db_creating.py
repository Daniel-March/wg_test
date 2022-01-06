import os
import sqlite3

import settings

if os.path.exists(settings.DATABASE_PATH):
    os.remove(settings.DATABASE_PATH)

connection = sqlite3.connect(settings.DATABASE_PATH)
connection.cursor()
cursor = connection.cursor()
cursor.execute("CREATE TABLE Engines ("
               "engine TEXT, "
               "power INTEGER, "
               "type INTEGER)")
cursor.execute("CREATE TABLE Hulls ("
               "hull TEXT, "
               "armor INTEGER, "
               "type INTEGER, "
               "capacity INTEGER)")
cursor.execute("CREATE TABLE Weapons ("
               "weapon TEXT, "
               "reload_speed INTEGER, "
               "rotation_speed INTEGER, "
               "diameter INTEGER, "
               "power_volley INTEGER, "
               "count INTEGER)")
cursor.execute("CREATE TABLE Ships ("
               "ship TEXT, "
               "weapon TEXT, "
               "hull TEXT, "
               "engine TEXT)")
cursor.close()
connection.commit()
connection.close()
