from typing import Any

from flask_sqlalchemy import SQLAlchemy

from .user_schema import UserInputSchema
from ...exceptions import UserEmailException, UserIdException

# Crear la instancia de SQLAlchemy
db = SQLAlchemy()


# Definir la clase User
class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    last_names = db.Column(db.String(50))
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(200))
    security_word = db.Column(db.String(50))
    matches = db.Column(db.Integer)
    wins = db.Column(db.Integer)

    def __init__(self, name, last_names, email, password, security_word):
        self.name = name
        self.last_names = last_names
        self.email = email
        self.password = password
        self.security_word = security_word

    def __repr__(self) -> str:
        """
        String representation of a user
        """
        return f'<User {self.name} ({self.email})>'

    @classmethod
    def create_user(cls, name: str, last_names: str, email: str, password: str, security_word: str) -> 'User':
        """
        Create a new user
        :param name:
        :param last_names:
        :param email:
        :param password:
        :param security_word:
        :return: The new user
        """
        # Crear un nuevo objeto de usuario
        new_user = User(
            name=name,
            last_names=last_names,
            email=email,
            password=password,
            security_word=security_word
        )
        # Agregar el nuevo usuario a la sesión
        db.session.add(new_user)
        # Confirmar los cambios en la base de datos
        db.session.commit()

        # Retornar el usuario recién creado
        return new_user

    @classmethod
    def modify_user(cls, name: str, last_names: str, email: str, password: str,
                    security_word: str) -> 'UserInputSchema':
        """
        Modify an existing user
        :param security_word:
        :param password:
        :param email:
        :param last_names:
        :param name:
        :return: The updated user
        """

        try:
            user = db.session.query(User).filter_by(email=email).first()

            if name:
                user.name = name
            if last_names:
                user.last_names = last_names
            if name:
                user.password = password
            if last_names:
                user.security_word = security_word

            try:
                db.session.commit()
                return user
            except Exception as e:
                db.session.rollback()
                raise e
        except Exception:
            raise UserEmailException()

    @classmethod
    def get_user_by_id(cls, user_id: int) -> 'User':
        """
        Modify an existing user
        :param user_id:
        :return: The searched user
        """

        try:
            return db.session.query(User).filter_by(id=user_id).first()
        except Exception:
            raise UserIdException()

    @classmethod
    def get_user_by_email(cls, user_email: email) -> 'User':
        """
        Modify an existing user
        :param user_email:
        :return: The searched user
        """

        try:
            return db.session.query(User).filter_by(email=user_email).first()
        except Exception:
            raise UserEmailException()

    @classmethod
    def delete_user_by_id(cls, user_id: int) -> None:
        """
        Modify an existing user
        :param user_id:
        :return: The searched user
        """

        try:
            user = db.session.query(User).filter_by(id=user_id).first()
            db.session.delete(user)
        except Exception:
            raise UserEmailException()

    @classmethod
    def delete_user_by_email(cls, user_email: email):
        """
        Modify an existing user
        :param user_email:
        :return: The searched user
        """

        try:
            user = db.session.query(User).filter_by(email=user_email).first()
            db.session.delete(user)
        except Exception:
            raise UserEmailException()

    @classmethod
    def get_all_users(cls) -> list[dict[str, Any]]:
        try:
            users = db.session.query(User).all()

            serialized_users = []
            for user in users:
                serialized_user = {
                    'name': user.name,
                    'last_names': user.last_names,
                    'email': user.email,
                    'password': user.password,
                    'security_word': user.security_word
                }
                serialized_users.append(serialized_user)

            return serialized_users
        except Exception:
            raise Exception("No existen usuarios.")

    @classmethod
    def change_user_password(cls, email: str, new_password: str):
        try:
            user = db.session.query(User).filter_by(email=email).first()
            user.password = new_password
            try:
                db.session.commit()
            except Exception as e:
                db.session.rollback()
                raise e
        except Exception:
            raise UserEmailException()

    @classmethod
    def add_new_win(cls, email: str):
        try:
            user = db.session.query(User).filter_by(email=email).first()
            user.matches += 1
            user.wins += 1

            try:
                db.session.commit()
                return {'matches': user.matches, 'wins': user.wins}
            except Exception as e:
                db.session.rollback()
                raise e
        except Exception:
            raise UserEmailException()

    @classmethod
    def add_new_match(cls, email: str):
        try:
            user = db.session.query(User).filter_by(email=email).first()
            user.matches += 1

            try:
                db.session.commit()
                return {'matches': user.matches}
            except Exception as e:
                db.session.rollback()
                raise e
        except Exception:
            raise UserEmailException()
