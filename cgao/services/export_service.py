from pathlib import Path

from cgao.exporters.csv_exporter import CSVExporter
from cgao.exporters.json_exporter import JSONExporter


class ExportService:

    def __init__(self):

        self.csv = CSVExporter()

        self.json = JSONExporter()

    def export_csv(self, posts, output):

        Path(output).parent.mkdir(

            parents=True,

            exist_ok=True,

        )

        self.csv.export(posts, output)

    def export_json(self, posts, output):

        Path(output).parent.mkdir(

            parents=True,

            exist_ok=True,

        )

        self.json.export(posts, output)