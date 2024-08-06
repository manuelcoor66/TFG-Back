from typing import Any

from sqlalchemy import and_

from src.models import db
from src.models.achievements.achievements_exceptions import (
    AchievementsException,
    AchievementExistsException,
)
from src.models.enrolments import Enrolment
from src.models.user import User


class Achievements(db.Model):
    __tablename__ = "achievements"
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String)
    table = db.Column(db.String)
    column = db.Column(db.String)
    amount = db.Column(db.Integer)

    def __init__(self, description, table, column, amount):
        self.description = description
        self.table = table
        self.column = column
        self.amount = amount

    def __repr__(self):
        return f"<Achievements(id={self.id}, description={self.description})>"

    @classmethod
    def get_all_achievements(cls) -> list[dict[str, Any]]:
        achievements = (
            db.session.query(Achievements)
            .order_by(Achievements.amount, Achievements.table)
            .all()
        )

        if achievements:
            serialized_achievements = []
            for achievement in achievements:
                serialized_achievement = {
                    "id": achievement.id,
                    "description": achievement.description,
                    "table": achievement.table,
                    "column": achievement.column,
                    "amount": achievement.amount,
                }

                serialized_achievements.append(serialized_achievement)

            return serialized_achievements
        else:
            raise AchievementsException

    @classmethod
    def create_achievements(
        cls, description: str, table: str, column: str, amount: int
    ) -> "Achievements":
        achievement = (
            db.session.query(Achievements)
            .filter(
                and_(
                    Achievements.table == table,
                    Achievements.column == column,
                    Achievements.amount == amount,
                )
            )
            .all()
        )

        if not achievement:
            new_achievement = Achievements(
                description=description, table=table, column=column, amount=amount
            )
            try:
                db.session.add(new_achievement)
                db.session.commit()
            except Exception as e:
                db.session.rollback()
                raise e

            return new_achievement
        else:
            raise AchievementExistsException

    @classmethod
    def get_user_achievements(cls, user_id: int):
        achievements = (
            db.session.query(Achievements).order_by(Achievements.amount).all()
        )
        user = User.get_user_by_id(user_id)

        serialized_achievements = []
        for achievement in achievements:
            if achievement.table == "user":
                serialized_achievement = {
                    "description": achievement.description,
                    "amount": achievement.amount,
                    "made": getattr(user, achievement.column, None),
                    "finalized": getattr(user, achievement.column, None)
                    >= achievement.amount,
                }

                serialized_achievements.append(serialized_achievement)

            if achievement.table == "enrolments":
                if achievement.column == "finalized":
                    winners = Enrolment.get_users_with_max_points_per_league()
                    isWinner = any(winner["user_id"] == user_id for winner in winners)
                    serialized_achievement = {
                        "description": achievement.description,
                        "amount": achievement.amount,
                        "made": 1 if isWinner else 0,
                        "finalized": isWinner,
                    }

                    serialized_achievements.append(serialized_achievement)
                else:
                    enrolments = (
                        db.session.query(Enrolment).filter_by(user_id=user_id).all()
                    )
                    serialized_achievement = {
                        "description": achievement.description,
                        "amount": achievement.amount,
                        "made": len(enrolments),
                        "finalized": len(enrolments) >= achievement.amount,
                    }

                    serialized_achievements.append(serialized_achievement)

        return serialized_achievements
