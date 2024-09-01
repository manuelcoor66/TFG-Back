from enum import Enum


class UserState(Enum):
    AVAILABLE = "AVAILABLE"
    BANNED = "BANNED"


class UserRole(Enum):
    USER = "USER"
    LEAGUEADMIN = "LEAGUEADMIN"
    ADMIN = "ADMIN"
