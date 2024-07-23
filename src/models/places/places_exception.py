class PlaceIdException(Exception):
    def __init__(self):
        self.message = "No se encontró ningún lugar con ese id."

        super().__init__(self.message)


class PlaceNameException(Exception):
    def __init__(self):
        self.message = "No se encontró ningún lugar con ese nombre."

        super().__init__(self.message)


class PlaceNameExistsException(Exception):
    def __init__(self):
        self.message = "Ya existe un lugar con ese nombre."

        super().__init__(self.message)
