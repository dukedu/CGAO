from __future__ import annotations

import argparse

from cgao.services import Pipeline


def build_parser():

    parser = argparse.ArgumentParser(

        prog="cgao",

        description="CGAO Research Framework",

    )

    sub = parser.add_subparsers(

        dest="command",

        required=True,

    )

    collect = sub.add_parser(

        "collect",

        help="Collect Xiaohongshu posts",

    )

    collect.add_argument(

        "--keyword",

        required=True,

    )

    collect.add_argument(

        "--limit",

        type=int,

        default=100,

    )

    collect.add_argument(

        "--csv",

        action="store_true",

    )

    collect.add_argument(

        "--json",

        action="store_true",

    )

    collect.add_argument(

        "--headless",

        action="store_true",

    )

    return parser


def collect(args):

    pipe = Pipeline()

    csv_path = (

        f"data/raw/{args.keyword}.csv"

        if args.csv

        else None

    )

    json_path = (

        f"data/raw/{args.keyword}.json"

        if args.json

        else None

    )

    posts = pipe.collect(

        keyword=args.keyword,

        limit=args.limit,

        csv=csv_path,

        json=json_path,

    )

    print()

    print("=" * 60)

    print(f"Keyword   : {args.keyword}")

    print(f"Collected : {len(posts)}")

    print("=" * 60)


def main():

    parser = build_parser()

    args = parser.parse_args()

    match args.command:

        case "collect":

            collect(args)


if __name__ == "__main__":

    main()