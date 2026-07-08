from dataclasses import dataclass, asdict


@dataclass
class Post:

    # 唯一标识
    note_id: str = ""

    # 搜索结果页参数
    xsec_token: str = ""
    xsec_source: str = ""

    # 基础信息
    title: str = ""
    author: str = ""
    like_count: int = 0

    # URL
    url: str = ""

    # ===== v0.3 详情页预留 =====

    author_id: str = ""

    content: str = ""

    publish_time: str = ""

    ip_location: str = ""

    collect_count: int = 0

    comment_count: int = 0

    share_count: int = 0

    image_count: int = 0

    tags: list[str] | None = None

    images: list[str] | None = None

    def __post_init__(self):

        if self.tags is None:
            self.tags = []

        if self.images is None:
            self.images = []

    def detail_url(self):

        if not self.note_id:
            return ""

        return (
            "https://www.xiaohongshu.com/explore/"
            f"{self.note_id}"
            f"?xsec_token={self.xsec_token}"
            "&xsec_source=pc_search"
        )

    def to_dict(self):

        data = asdict(self)

        data["detail_url"] = self.detail_url()

        return data