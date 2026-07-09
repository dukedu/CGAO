from pathlib import Path
from dataclasses import asdict, is_dataclass

from openpyxl import Workbook


class ExcelExporter:

    def export(self, posts, filepath):

        filepath = Path(filepath)

        filepath.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        if len(posts) == 0:
            print("No posts to export.")
            return

        rows = [
            asdict(post) if is_dataclass(post) else post.to_dict()
            for post in posts
        ]

        workbook = Workbook()

        sheet = workbook.active

        sheet.title = "posts"

        headers = list(rows[0].keys())

        sheet.append(headers)

        for row in rows:

            sheet.append(
                [row.get(key) for key in headers]
            )

        workbook.save(filepath)

        print(f"\nExcel exported to:\n{filepath.resolve()}")
