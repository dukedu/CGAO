from __future__ import annotations

import time


def retry(

    retries=3,

    delay=1,

    exceptions=(Exception,),

):

    def wrapper(func):

        def inner(*args, **kwargs):

            last = None

            for _ in range(retries):

                try:

                    return func(

                        *args,

                        **kwargs,

                    )

                except exceptions as e:

                    last = e

                    time.sleep(delay)

            raise last

        return inner

    return wrapper