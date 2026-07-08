import json
from dataclasses import asdict, is_dataclass


class JSONExporter:

    def export(self, data, path):

        rows = []

        for item in data:

            if is_dataclass(item):

                rows.append(asdict(item))

            else:

                rows.append(item)

        with open(

            path,

            "w",

            encoding="utf-8",

        ) as f:

            json.dump(

                rows,

                f,

                ensure_ascii=False,

                indent=2,

            )

        print(f"\nJSON exported to:\n{path}")