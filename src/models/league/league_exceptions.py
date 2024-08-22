class LeagueExistsException(Exception):
    def __init__(self):
        self.message = "Ya existe una liga con ese nombre."

        super().__init__(self.message)

    def __str__(self):
        return f"{self.message}"


class LeagueIdException(Exception):
    def __init__(self):
        self.message = "No se encontró ninguna liga con ese id."

        super().__init__(self.message)

    def __str__(self):
        return f"{self.message}"


class LeagueNameException(Exception):
    def __init__(self):
        self.message = "No se encontró ninguna liga con ese nombre."

        super().__init__(self.message)

    def __str__(self):
        return f"{self.message}"
