import random
import string
from datetime import date

from sqlalchemy import Column, ForeignKey, Integer, String, DATE
from sqlalchemy.orm import Session, relationship

from settings import Config
from database import Database
from components.users.tasks import email_verification_task


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
            user_role = Config.role["user"],
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
    def update_profile(cls, db_session: Session, data):
        user_update = db_session.query(User).filter(
            User.username == data["username"]
        ).first()

        if data["firstname"] is not None:
            user_update.first_name = data["firstname"]
        if data["surname"] is not None:
            user_update.surname = data["surname"]

        try:
            db_session.add(user_update)
            db_session.commit()
            return True
        except Exception as e:
            print(e)
            return False


    @classmethod
    def update_user_password(cls, db_session: Session, data):
        user = db_session.query(User).filter(
            User.username == data["username"]
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


    @classmethod
    def avatar_update(cls, db_session: Session, login, filepath):
        user = db_session.query(User).filter(
            User.username == login
        ).first()
        user.avatar = filepath
        try:
            db_session.add(user)
            db_session.commit()
            return True
        except Exception as e:
            print(e)
            return False


class UserVerification(Database.Base):
    __tablename__ = 'users_verification_email'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    code = Column(String(255), nullable=False, unique=True)
    

    def __repr__(self):
        return f"Email_token {self.id}"

    @classmethod
    def create_verification_code(cls, db_session: Session, data):
        verification_code = ''.join(random.choice(string.ascii_lowercase) for i in range(20))
        verification_link = Config.BASE_URL+"auth/verified/"+verification_code
        user = db_session.query(User).filter(
            User.username == data["username"]
        ).first()

        email_verification_task.delay(data['email'], verification_link)
        
        new_code = UserVerification(
            user_id = user.id,
            code = verification_code
        )
        try:
            db_session.add(new_code)
            db_session.commit()
            return True
        except Exception as e:
            print(e)
            return False

    @classmethod
    def verification_user(cls, db_session: Session, code):
        code_obj = db_session.query(UserVerification).filter(
            UserVerification.code == code
        ).first()
        if code_obj is not None:
            user_data = db_session.query(User).filter(
                User.id == code_obj.user_id
            ).first()
            
            user_data.email_verified_at = date.today()
            user_data.user_role = Config.role["user_verified"]
            try:
                db_session.add(user_data)
                db_session.commit()
                return True
            except Exception as e:
                print(e)
                return False
        else:
            return False

    @classmethod
    def delete_code(cls, db_session: Session, code):
        code = db_session.query(UserVerification).filter(
            UserVerification.code == code
        ).first()
        db_session.delete(code)
        db_session.commit()