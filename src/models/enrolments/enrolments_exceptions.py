class EnrolmentIdException(Exception):
    def __init__(self):
        self.message = "No se encontró ninguna matricula con ese id."

        super().__init__(self.message)


class EnrolmentUserIdException(Exception):
    def __init__(self):
        self.message = "No se encontró ninguna matricula de ese usuario."

        super().__init__(self.message)


class EnrolmentLeagueIdException(Exception):
    def __init__(self):
        self.message = "No se encontró ninguna matricula de esa liga."

        super().__init__(self.message)


class EnrolmentsException(Exception):
    def __init__(self):
        self.message = "No se encontró ninguna matricula."

        super().__init__(self.message)


class EnrolmentException(Exception):
    def __init__(self):
        self.message = "No se encontró ninguna matricula."

        super().__init__(self.message)
