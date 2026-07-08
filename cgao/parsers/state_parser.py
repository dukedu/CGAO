import json
import re


class StateParser:

    @staticmethod
    def parse(html: str):

        m = re.search(
            r"window\.__INITIAL_STATE__\s*=\s*(\{.*?\})\s*</script>",
            html,
            re.S,
        )

        if m is None:

            m = re.search(
                r"window\.__INITIAL_STATE__\s*=\s*(\{.*)",
                html,
                re.S,
            )

        if m is None:

            raise RuntimeError("Cannot find __INITIAL_STATE__")

        text = m.group(1)

        # 去掉最后可能的 </script>
        idx = text.find("</script>")

        if idx != -1:

            text = text[:idx]

        text = text.strip()

        if text.endswith(";"):

            text = text[:-1]

        text = text.replace(":undefined", ":null")
        text = text.replace(":NaN", ":null")
        text = text.replace(":Infinity", ":null")

        return json.loads(text)