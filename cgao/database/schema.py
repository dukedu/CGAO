from __future__ import annotations

from sqlite3 import Connection


def create_tables(conn: Connection):

    conn.execute("""
    CREATE TABLE IF NOT EXISTS authors(

        author_id TEXT PRIMARY KEY,

        nickname TEXT,

        avatar TEXT,

        xsec_token TEXT,

        description TEXT,

        gender TEXT,

        follower_count INTEGER DEFAULT 0,

        following_count INTEGER DEFAULT 0,

        note_count INTEGER DEFAULT 0,

        liked_count INTEGER DEFAULT 0,

        verified INTEGER DEFAULT 0

    )
    """)

    conn.execute("""
    CREATE TABLE IF NOT EXISTS posts(

        note_id TEXT PRIMARY KEY,

        author_id TEXT,

        title TEXT,

        content TEXT,

        publish_time TEXT,

        ip_location TEXT,

        like_count INTEGER,

        collect_count INTEGER,

        comment_count INTEGER,

        share_count INTEGER,

        xsec_token TEXT,

        FOREIGN KEY(author_id)

        REFERENCES authors(author_id)

    )
    """)

    conn.execute("""
    CREATE TABLE IF NOT EXISTS images(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        note_id TEXT,

        url TEXT,

        width INTEGER,

        height INTEGER,

        file_id TEXT,

        format TEXT,

        size INTEGER,

        image_order INTEGER,

        FOREIGN KEY(note_id)

        REFERENCES posts(note_id)

    )
    """)

    conn.execute("""
    CREATE TABLE IF NOT EXISTS tags(

        tag_id INTEGER PRIMARY KEY AUTOINCREMENT,

        name TEXT UNIQUE,

        use_count INTEGER DEFAULT 0,

        view_count INTEGER DEFAULT 0

    )
    """)

    conn.execute("""
    CREATE TABLE IF NOT EXISTS post_tags(

        note_id TEXT,

        tag_id INTEGER,

        PRIMARY KEY(

            note_id,

            tag_id

        ),

        FOREIGN KEY(note_id)

        REFERENCES posts(note_id),

        FOREIGN KEY(tag_id)

        REFERENCES tags(tag_id)

    )
    """)

    conn.execute("""
    CREATE TABLE IF NOT EXISTS comments(

        comment_id TEXT PRIMARY KEY,

        note_id TEXT,

        author_id TEXT,

        content TEXT,

        publish_time TEXT,

        like_count INTEGER,

        reply_count INTEGER,

        ip_location TEXT

    )
    """)

    conn.commit()