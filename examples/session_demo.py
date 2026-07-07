from cgao.crawler.session import SessionManager

session = SessionManager()

page = session.new_page()

page.goto("https://www.baidu.com")

input("Press Enter after login...")

session.save_cookie()

session.close()