from sqlalchemy import Column, ForeignKey, Integer, String, TEXT, BOOLEAN, DateTime
from sqlalchemy.orm import Session, relationship
""" from components.game_event.model import GameEvent """

from settings import Config
from database import Database

class GameCampaign(Database.Base):
    __tablename__ = "game_campaigns"

    id = Column(Integer, primary_key=True)
    campaign_name = Column(String(255), nullable=False)

    """ game_event = relationship("GameEvent", primaryjoin=GameEvent.id_game_campaign) """

    def __repr__(self):
        return f"GameCampaign {self.id}"