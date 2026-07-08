from __future__ import annotations

from cgao.database.sqlite import SQLite


class Repository:

    def __init__(

        self,

        db: SQLite,

    ):

        self.db = db

    def execute(

        self,

        sql,

        params=(),

    ):

        return self.db.execute(

            sql,

            params,

        )

    def fetchone(

        self,

        sql,

        params=(),

    ):

        return self.execute(

            sql,

            params,

        ).fetchone()

    def fetchall(

        self,

        sql,

        params=(),

    ):

        return self.execute(

            sql,

            params,

        ).fetchall()

    def commit(self):

        self.db.commit()