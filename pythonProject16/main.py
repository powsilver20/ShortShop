import sqlite3
from flask import Flask
query = "CREATE TABLE Products ("\
        "id varchar(230) PRIMARY KEY," \
        "image BLOB NOT NULL)"
drop = "DROP TABLE Products"
db = sqlite3.connect("database/product.db")
cursor = db.cursor()
cursor.execute(query)

