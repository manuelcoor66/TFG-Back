class UserEmailException(Exception):
    def __init__(self):
        self.message = "No se encontró ningún usuario con ese correo electrónico."

        super().__init__(self.message)

    def __str__(self):
        return f"{self.message}"


class UserIdException(Exception):
    def __init__(self):
        self.message = "No se encontró ningún usuario con ese id."

        super().__init__(self.message)

    def __str__(self):
        return f"{self.message}"