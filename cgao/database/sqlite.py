from __future__ import annotations

import sqlite3

from cgao.core import DATABASE_PATH

from .schema import create_tables


class SQLite:

    def __init__(

        self,

        path=DATABASE_PATH,

    ):

        self.conn = sqlite3.connect(path)

        self.conn.execute(

            "PRAGMA foreign_keys=ON"

        )

        create_tables(

            self.conn

        )

    def execute(

        self,

        sql,

        params=(),

    ):

        return self.conn.execute(

            sql,

            params,

        )

    def executemany(

        self,

        sql,

        params,

    ):

        return self.conn.executemany(

            sql,

            params,

        )

    def commit(self):

        self.conn.commit()

    def rollback(self):

        self.conn.rollback()

    def close(self):

        self.conn.close()