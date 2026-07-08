from pathlib import Path
import csv


class CSVExporter:

    def export(self, posts, filepath):

        filepath = Path(filepath)

        filepath.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        if len(posts) == 0:
            print("No posts to export.")
            return

        with open(
            filepath,
            "w",
            newline="",
            encoding="utf-8-sig"
        ) as f:

            writer = csv.DictWriter(
                f,
                fieldnames=posts[0].to_dict().keys()
            )

            writer.writeheader()

            for post in posts:

                writer.writerow(
                    post.to_dict()
                )

        print(f"\nCSV exported to:\n{filepath.resolve()}")