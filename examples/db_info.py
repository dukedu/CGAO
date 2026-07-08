from pathlib import Path
import sqlite3


DB_PATH = Path("data/database/cgao.db")


if not DB_PATH.exists():

    print("Database not found.")

    raise SystemExit


conn = sqlite3.connect(DB_PATH)

cursor = conn.cursor()


def count(table):

    try:

        cursor.execute(f"SELECT COUNT(*) FROM {table}")

        return cursor.fetchone()[0]

    except:

        return 0


posts = count("posts")
authors = count("authors")
keywords = count("keywords")
images = count("images")


csv_files = list(Path("data/raw").glob("*.csv"))


print()
print("=" * 60)
print("CGAO Database Information")
print("=" * 60)
print(f"Database : {DB_PATH}")
print(f"Size     : {DB_PATH.stat().st_size / 1024 / 1024:.2f} MB")
print()
print(f"Posts    : {posts}")
print(f"Authors  : {authors}")
print(f"Keywords : {keywords}")
print(f"Images   : {images}")
print()
print(f"CSV Files: {len(csv_files)}")

for f in sorted(csv_files):

    print(f"  └── {f.name}")

print("=" * 60)

conn.close()