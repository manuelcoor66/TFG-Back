class TicketIdException(Exception):
    def __init__(self):
        self.message = "No se encontró ninguna ticket con ese id."

        super().__init__(self.message)


class TicketsException(Exception):
    def __init__(self):
        self.message = "No se encontró ningun ticket."

        super().__init__(self.message)


class UserTicketsException(Exception):
    def __init__(self):
        self.message = "No se encontró ningun ticket de ese usuario."

        super().__init__(self.message)
