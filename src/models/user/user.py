from flask_sqlalchemy import SQLAlchemy

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
