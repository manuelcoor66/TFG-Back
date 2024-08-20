from enum import Enum


class TicketState(Enum):
    PAID = "paid"
    INPROGRESS = "inProgress"
    REJECTED = "rejected"
