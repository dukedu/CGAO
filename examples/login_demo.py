from cgao.crawler.browser import Browser

browser = Browser(
    headless=False
)

browser.start()

page = browser.new_page()

page.goto(
    "https://www.xiaohongshu.com/explore"
)

print()

print("=" * 60)

print("请扫码登录小红书")

print("登录成功以后")

print("回到终端按 Enter")

print("=" * 60)

input()

browser.save_state()

browser.stop()