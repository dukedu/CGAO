from cgao.crawler.browser import Browser

browser = Browser()

browser.start()

page = browser.new_page()

page.goto("https://www.baidu.com")

print(page.title())

input("Press Enter to quit...")

browser.close()