from __future__ import annotations

import time


class Timer:

    def __enter__(self):

        self.start = time.perf_counter()

        return self

    def __exit__(

        self,

        *_,

    ):

        self.end = time.perf_counter()

        self.elapsed = (

            self.end

            - self.start

        )