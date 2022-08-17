class DisneyPlus:
    def __init__(self) -> None:
        self.name = "Disney+"
        self.code = "dnp"

    def get_code(self):
        return self.code

    def __str__(self) -> str:
        return self.name