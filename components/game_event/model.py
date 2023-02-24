from datetime import datetime

from sqlalchemy import Column, ForeignKey, Integer, String, TEXT, BOOLEAN, DateTime
from sqlalchemy.orm import Session, relationship

from settings import Config
from database import Database


class GameEvent(Database.Base):
    __tablename__ = 'game_events'

    id = Column(Integer, primary_key=True)
    id_creator = Column(Integer, ForeignKey('users.id'))
    date_event = Column(DateTime(timezone=True), nullable=False)
    loscut = Column(String, nullable=False)
    description = Column(TEXT, default="There is no description")
    online = Column(BOOLEAN, default=False)
    privacy = Column(BOOLEAN, default=False)
    venue = Column(TEXT, nullable=True) # Место проведения события если офлайн
    id_master = Column(Integer, ForeignKey("users.id"))
    connected_players_count = Column(Integer, default=0)
    game_status = Column(BOOLEAN, default=True)

    

    def __repr__(self):
        return f"GameEvent {self.id}"


    @classmethod
    def creating_an_event(cls, db_session: Session, data: dict):
        if data["date_event"] <= datetime.now():
            return False
        
        new_event = GameEvent(
            id_creator = data["user_id"],
            date_event = data["date_event"],
            loscut = data["loscut"],
            description = data["description"] if data.get("description") else "There is no description",
            online = data['online'],
            privacy = data["privacy"],
            venue = data["venue"],
            id_master = data["id_master"] if data.get("id_master") else None
        )
        try:
            db_session.add(new_event)
            db_session.commit()
            return True
        except Exception as e:
            print(e)
            return False

    @classmethod
    def get_events(cls, db_session: Session, data: dict = None):
        events = db_session.query(GameEvent).all()
        return events


class UsersGameEvents(Database.Base):
    __tablename__ = "users_game_events"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    event_id = Column(Integer, ForeignKey("game_events.id"))

    def __repr__(self):
        return f"UsersGameEvents {self.id}"


    @classmethod
    def user_subscribes(cls, db_session: Session, data):
        new_subscription = UsersGameEvents(
            user_id = data["user_id"],
            event_id = data["event_id"]
        )
        try:
            db_session.add(new_subscription)
            db_session.commit()
            return True
        except Exception as e:
            print(e)
            return False
