from cgao.collector import SearchCollector
from cgao.core import Browser
from cgao.pages.home_page import HomePage

browser = Browser()

browser.start()

page = browser.new_page()

home = HomePage(page)

home.open()

home.search("DeepSeek")

posts = SearchCollector(page).collect(limit=5)

print(posts)

browser.stop()