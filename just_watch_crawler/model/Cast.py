


class Cast:
    def __init__(self, credit) -> None:
        self.name = credit['name']
        self.character_name = credit['character_name']
    
    def __str__(self) -> str:
        return "{} ({})".format(self.name, self.character_name)