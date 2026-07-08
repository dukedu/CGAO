import sqlite3

from cgao.database.schema import create_tables


conn = sqlite3.connect(
    "data/database/cgao.db"
)

create_tables(conn)

print()

cursor = conn.execute(

    "SELECT name FROM sqlite_master WHERE type='table'"

)

for row in cursor:

    print(row[0])

conn.close()