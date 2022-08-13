

class Netflix:
    def __init__(self) -> None:
        self.name = "Netflix"
        self.code = "nfx"

    def get_code(self):
        return self.code

    def __str__(self) -> str:
        return self.name