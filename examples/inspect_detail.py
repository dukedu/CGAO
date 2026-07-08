from cgao.crawler.xiaohongshu import XiaohongshuCrawler

crawler = XiaohongshuCrawler()

try:

    crawler.open()

    crawler.search("DeepSeek")

    posts = crawler.collect(limit=1)

    if not posts:

        raise Exception("No posts found.")

    post = posts[0]

    print(post.detail_url())

    crawler.page.goto(
        post.detail_url(),
        wait_until="domcontentloaded"
    )

    crawler.page.wait_for_timeout(5000)

    html = crawler.page.content()

    with open(
        "detail.html",
        "w",
        encoding="utf-8"
    ) as f:

        f.write(html)

    print("detail.html saved.")

finally:

    crawler.close()