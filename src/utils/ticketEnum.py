from enum import Enum


class TicketState(Enum):
    PAID = "paid"
    IN_PROGRESS = "inProgress"
    REJECTED = "rejected"
