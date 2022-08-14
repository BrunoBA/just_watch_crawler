


class Cast:
    def __init__(self, credit) -> None:
        self.__initialize_properties(credit)

    def __initialize_properties(self, credit):
        properties = ['name' ,'character_name']

        for property in properties:
            if property in credit:
                setattr(self, property, credit[property])
            else:
                setattr(self, property, "")
    
    def __str__(self) -> str:
        return "{} ({})".format(self.name, self.character_name)