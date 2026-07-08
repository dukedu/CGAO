import sqlite3


conn = sqlite3.connect(
    "data/database/cgao.db"
)

cursor = conn.cursor()

cursor.execute(

    """
    SELECT

        title,

        author,

        like_count

    FROM posts

    ORDER BY like_count DESC

    LIMIT 20
    """

)

for row in cursor.fetchall():

    print(row)

conn.close()