class AchievementsException(Exception):
    def __init__(self):
        self.message = "No se encontró ningún logro."

        super().__init__(self.message)


class AchievementExistsException(Exception):
    def __init__(self):
        self.message = "Ya existe ese logro."

        super().__init__(self.message)
