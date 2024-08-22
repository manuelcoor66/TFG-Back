class UserWithMatch(Exception):
    def __init__(self):
        self.message = "El usuario ya tiene un partido en esa liga."

        super().__init__(self.message)

    def __str__(self):
        return f"{self.message}"


# class UserWithMatch(Exception):
#     def __init__(self):
#         self.message = "El usuario ya tiene un partido en esa liga."
#
#         super().__init__(self.message)
#
#     def __str__(self):
#         return f"{self.message}"


class MatchesLeagueIdException(Exception):
    def __init__(self):
        self.message = "No se encontró ningún partido de esa liga."

        super().__init__(self.message)
