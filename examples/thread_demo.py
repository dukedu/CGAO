from time import perf_counter

from cgao.collector import (
    SearchCollector,
    ThreadedDetailCollector,
)
from cgao.core import Browser
from cgao.pages.home_page import HomePage


browser = Browser()

browser.start()

page = browser.new_page()

home = HomePage(page)

home.open()

home.search("DeepSeek")

search = SearchCollector(page)

posts = search.collect(limit=20)

browser.stop()

start = perf_counter()

collector = ThreadedDetailCollector(

    workers=5,

)

results = collector.collect(posts)

end = perf_counter()

print()

print("=" * 60)

print(f"Posts : {len(results)}")

print(f"Time  : {end-start:.2f}s")

print("=" * 60)