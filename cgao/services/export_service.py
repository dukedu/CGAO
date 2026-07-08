from __future__ import annotations

from pathlib import Path

from cgao.exporters.csv_exporter import CSVExporter
from cgao.exporters.json_exporter import JSONExporter


class ExportService:

    def __init__(self):

        self.csv = CSVExporter()

        self.json = JSONExporter()

    def csv_export(

        self,

        posts,

        path,

    ):

        Path(path).parent.mkdir(

            parents=True,

            exist_ok=True,

        )

        self.csv.export(

            posts,

            path,

        )

    def json_export(

        self,

        posts,

        path,

    ):

        Path(path).parent.mkdir(

            parents=True,

            exist_ok=True,

        )

        self.json.export(

            posts,

            path,

        )