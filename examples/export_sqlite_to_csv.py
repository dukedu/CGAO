import sqlite3
import csv
from pathlib import Path


DB_PATH = "data/database/cgao.db"
CSV_PATH = "data/raw/DeepSeek.csv"

Path("data/raw").mkdir(
    parents=True,
    exist_ok=True
)

conn = sqlite3.connect(DB_PATH)

cursor = conn.cursor()

cursor.execute(
    """
    SELECT
        note_id,
        title,
        author,
        like_count,
        url,
        xsec_token
    FROM posts
    """
)

rows = cursor.fetchall()

with open(
    CSV_PATH,
    "w",
    newline="",
    encoding="utf-8-sig"
) as f:

    writer = csv.writer(f)

    writer.writerow([
        "note_id",
        "title",
        "author",
        "like_count",
        "url",
        "xsec_token",
    ])

    writer.writerows(rows)

conn.close()

print("=" * 60)
print(f"Exported {len(rows)} posts")
print(f"CSV Saved -> {CSV_PATH}")
print("=" * 60)