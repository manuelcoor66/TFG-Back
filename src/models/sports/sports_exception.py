class SportIdException(Exception):
    def __init__(self):
        self.message = "No se encontró ningún deporte con ese id."

        super().__init__(self.message)


class SportNameException(Exception):
    def __init__(self):
        self.message = "No se encontró ningún deporte con ese nombre."

        super().__init__(self.message)


class SportException(Exception):
    def __init__(self):
        self.message = "No se encontró ningún deporte."

        super().__init__(self.message)


class SportNameExistsException(Exception):
    def __init__(self):
        self.message = "Ya existe un deporte con ese nombre."

        super().__init__(self.message)
