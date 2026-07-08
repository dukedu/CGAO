from pathlib import Path
from pprint import pformat

from cgao.parsers.state_parser import StateParser

html = Path("detail.html").read_text(encoding="utf-8")

state = StateParser.parse(html)

Path("note.txt").write_text(
    pformat(state["note"], width=120),
    encoding="utf-8"
)

print("note.txt saved.")