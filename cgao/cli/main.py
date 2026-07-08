import argparse

from cgao.services import (

    CrawlerService,

    ExportService,

)


def collect(args):

    crawler = CrawlerService()

    exporter = ExportService()

    posts = crawler.collect(

        keyword=args.keyword,

        limit=args.limit,

    )

    if args.csv:

        exporter.export_csv(

            posts,

            f"data/raw/{args.keyword}.csv",

        )

    if args.json:

        exporter.export_json(

            posts,

            f"data/raw/{args.keyword}.json",

        )

    print()

    print("=" * 60)

    print(f"Keyword : {args.keyword}")

    print(f"Collected : {len(posts)}")

    print("=" * 60)


def main():

    parser = argparse.ArgumentParser(

        prog="cgao"

    )

    sub = parser.add_subparsers(

        dest="command",

    )

    collect_parser = sub.add_parser(

        "collect",

    )

    collect_parser.add_argument(

        "--keyword",

        required=True,

    )

    collect_parser.add_argument(

        "--limit",

        type=int,

        default=100,

    )

    collect_parser.add_argument(

        "--csv",

        action="store_true",

    )

    collect_parser.add_argument(

        "--json",

        action="store_true",

    )

    args = parser.parse_args()

    if args.command == "collect":

        collect(args)


if __name__ == "__main__":

    main()