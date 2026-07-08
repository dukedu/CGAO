from __future__ import annotations

from cgao.database import SQLite
from cgao.models import DetailResult


class DatabaseService:

    def __init__(self):

        self.db = SQLite()

    def save(self, result: DetailResult):

        self.save_author(result)
        self.save_post(result)
        self.save_images(result)
        self.save_tags(result)

        self.db.commit()

    def save_author(self, result):

        a = result.author

        self.db.execute(
            """
            INSERT OR REPLACE INTO authors(
                author_id,
                nickname,
                avatar,
                xsec_token,
                description,
                gender,
                follower_count,
                following_count,
                note_count,
                liked_count,
                verified
            )
            VALUES(?,?,?,?,?,?,?,?,?,?,?)
            """,
            (
                a.author_id,
                a.nickname,
                a.avatar,
                a.xsec_token,
                a.description,
                a.gender,
                a.follower_count,
                a.following_count,
                a.note_count,
                a.liked_count,
                int(a.verified),
            ),
        )

    def save_post(self, result):

        p = result.post

        self.db.execute(
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

    def save_images(self, result):

        self.db.execute(
            "DELETE FROM images WHERE note_id=?",
            (result.post.note_id,),
        )

        for img in result.images:

            self.db.execute(
                """
                INSERT INTO images(
                    note_id,
                    url,
                    width,
                    height,
                    file_id,
                    format,
                    size,
                    image_order
                )
                VALUES(?,?,?,?,?,?,?,?)
                """,
                (
                    img.note_id,
                    img.url,
                    img.width,
                    img.height,
                    img.file_id,
                    img.format,
                    img.size,
                    img.order,
                ),
            )

    def save_tags(self, result):

        self.db.execute(
            "DELETE FROM post_tags WHERE note_id=?",
            (result.post.note_id,),
        )

        for tag in result.tags:

            self.db.execute(
                """
                INSERT OR IGNORE INTO tags(name)
                VALUES(?)
                """,
                (tag.name,),
            )

            tag_id = self.db.execute(
                """
                SELECT tag_id
                FROM tags
                WHERE name=?
                """,
                (tag.name,),
            ).fetchone()[0]

            self.db.execute(
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

        self.db.close()