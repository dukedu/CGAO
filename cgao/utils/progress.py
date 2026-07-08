class Progress:

    def __init__(

        self,

        total,

    ):

        self.total = total

        self.current = 0

    def update(self):

        self.current += 1

        print(

            f"\r[{self.current}/{self.total}]",

            end="",

            flush=True,

        )

    def finish(self):

        print()