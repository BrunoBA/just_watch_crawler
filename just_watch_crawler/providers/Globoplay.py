class Globoplay:
    def __init__(self) -> None:
        self.name = "Globoplay"
        self.code = "gop"

    def get_code(self):
        return self.code

    def __str__(self) -> str:
        return self.name