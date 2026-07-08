from pathlib import Path
import sqlite3


class SQLiteDatabase:

    def __init__(self, db="data/database/cgao.db"):

        Path(db).parent.mkdir(
            parents=True,
            exist_ok=True
        )

        self.conn = sqlite3.connect(db)

        self.create()

    def create(self):

        self.conn.execute(
            """
            CREATE TABLE IF NOT EXISTS posts(

                note_id TEXT PRIMARY KEY,

                title TEXT,

                author TEXT,

                like_count INTEGER,

                url TEXT,

                xsec_token TEXT

            )
            """
        )

        self.conn.commit()

    def insert(self, post):

        self.conn.execute(

            """
            INSERT OR REPLACE INTO posts

            VALUES (?,?,?,?,?,?)
            """,

            (

                post.note_id,

                post.title,

                post.author,

                post.like_count,

                post.url,

                post.xsec_token

            )

        )

    def save(self):

        self.conn.commit()

    def close(self):

        self.conn.close()
    
    def exists(self, note_id):

        cursor = self.conn.execute(

            """
            SELECT 1

            FROM posts

            WHERE note_id=?

            LIMIT 1
            """,

            (note_id,)

    )

        return cursor.fetchone() is not None

    def count(self):

        cursor = self.conn.execute(

            """
            SELECT COUNT(*)

            FROM posts
            """

        )

        return cursor.fetchone()[0]