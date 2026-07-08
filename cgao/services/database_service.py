import sqlite3

from cgao.models import DetailResult


class DatabaseService:

    def __init__(self, db_path: str):

        self.conn = sqlite3.connect(db_path)

        self.conn.execute("PRAGMA foreign_keys = ON")

    def save(self, result: DetailResult):

        self._save_author(result)

        self._save_post(result)

        self._save_images(result)

        self._save_tags(result)

        self.conn.commit()

    def _save_author(self, result):

        a = result.author

        self.conn.execute(

            """
            INSERT OR REPLACE INTO authors
            (author_id,nickname,avatar,xsec_token)
            VALUES(?,?,?,?)
            """,

            (

                a.author_id,

                a.nickname,

                a.avatar,

                a.xsec_token,

            ),

        )

    def _save_post(self, result):

        p = result.post

        self.conn.execute(

            """
            INSERT OR REPLACE INTO posts(

                note_id,

                author_id,

                title,

                content,

                publish_time,

                ip_location,

                like_count,

                collect_count,

                comment_count,

                share_count,

                xsec_token

            )

            VALUES(?,?,?,?,?,?,?,?,?,?,?)
            """,

            (

                p.note_id,

                p.author_id,

                p.title,

                p.content,

                p.publish_time,

                p.ip_location,

                p.like_count,

                p.collect_count,

                p.comment_count,

                p.share_count,

                p.xsec_token,

            ),

        )

    def _save_images(self, result):

        self.conn.execute(

            "DELETE FROM images WHERE note_id=?",

            (result.post.note_id,),

        )

        for img in result.images:

            self.conn.execute(

                """
                INSERT INTO images(

                    note_id,

                    url,

                    width,

                    height

                )

                VALUES(?,?,?,?)
                """,

                (

                    img.note_id,

                    img.url,

                    img.width,

                    img.height,

                ),

            )

    def _save_tags(self, result):

        self.conn.execute(

            "DELETE FROM post_tags WHERE note_id=?",

            (result.post.note_id,),

        )

        for tag in result.tags:

            self.conn.execute(

                """
                INSERT OR IGNORE INTO tags(name)

                VALUES(?)
                """,

                (

                    tag.name,

                ),

            )

            tag_id = self.conn.execute(

                """
                SELECT tag_id

                FROM tags

                WHERE name=?
                """,

                (

                    tag.name,

                ),

            ).fetchone()[0]

            self.conn.execute(

                """
                INSERT INTO post_tags(

                    note_id,

                    tag_id

                )

                VALUES(?,?)
                """,

                (

                    result.post.note_id,

                    tag_id,

                ),

            )

    def close(self):

        self.conn.close()