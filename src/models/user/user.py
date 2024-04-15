from flask_sqlalchemy import SQLAlchemy

from .user_schema import UserInputSchema

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
    def modify_user(cls, name: str, last_names: str, email: str, password: str, security_word: str) -> 'UserInputSchema':
        """
        Modify an existing user
        :param security_word:
        :param password:
        :param email:
        :param last_names:
        :param name:
        :param user_changed:
        :return: The updated user
        """

        user = db.session.query(User).filter_by(email=email).first()

        if user:
            user.name = name
            user.last_names = last_names
            user.password = password
            user.security_word = security_word

            try:
                db.session.commit()
                return user
            except Exception as e:
                db.session.rollback()
                raise e
        else:
            raise Exception("No se encontró ningún usuario con ese correo electrónico.")

    @classmethod
    def get_user_by_id(cls, user_id: int) -> 'User':
        """
        Modify an existing user
        :param user_id:
        :return: The updated user
        """

        try:
            return db.session.query(User).filter_by(id=user_id).first()
        except Exception:
            raise Exception("No se encontró ningún usuario con ese correo electrónico.")