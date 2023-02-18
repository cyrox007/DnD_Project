import random
import string

from sqlalchemy import Column, Integer, String, DATE, ForeignKey
from sqlalchemy.orm import Session

from apps.site.settings import Config
from database import Database

""" from werkzeug.security import generate_password_hash, check_password_hash """


class User(Database.Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    email = Column(String(255), nullable=False, unique=True)
    username = Column(String(255), nullable=False, unique=True)
    password = Column(String(255), nullable=False)
    first_name = Column(String(255), nullable=True, default="Is unknown")
    surname = Column(String(255), nullable=True, default="Is unknown")
    user_role = Column(Integer, nullable=False)
    avatar = Column(String(), nullable=False)
    email_verified_at = Column(DATE, nullable=True)
    remember_token = Column(String(100))
    
    def __repr__(self):
        return f"User {self.id}"

    @classmethod
    def get_user(cls, db_session: Session, login):
        return db_session.query(User).filter(
            User.username == login
        ).first()


    @classmethod
    def insert_new_user(cls, db_session: Session, data: dict):
        new_user = User(
            email = data['email'],
            username = data['username'],
            password = data['password'],
            user_role = 100,
            avatar = Config.AVATAR_DIR+"default_avatar.png",
            remember_token = ''.join(random.choice(string.ascii_lowercase) for i in range(10))
        )
        try:
            db_session.add(new_user)
            db_session.commit()
            return True
        except Exception as e:
            print(e)
            return False

    
    @classmethod
    def update_profile(db_session: Session, data):
        user_update = db_session.query(User).filter(
            "username" == data["username"]
        ).first()

        if data["firstname"] is not "":
            user_update.first_name = data["firstname"]
        if data["surname"] is not "":
            user_update.surname = data["surname"]

        try:
            db_session.add(user_update)
            db_session.commit()
            return True
        except Exception as e:
            print(e)
            return False


    @classmethod
    def update_user_password(db_session: Session, data):
        user = db_session.query(User).filter(
            "username" == data["username"]
        ).first()

        if user.password != data["userpassword"]:
            print("Неверный пароль")
            return False
        
        user.password = data["newpassword"]

        try:
            db_session.add(user)
            db_session.commit()
            return True
        except Exception as e:
            print(e)
            return False