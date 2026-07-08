class XHSUrl:

    @staticmethod
    def detail(note_id, token):

        return (
            "https://www.xiaohongshu.com/explore/"
            f"{note_id}"
            f"?xsec_token={token}"
            "&xsec_source=pc_search"
        )