from components.game_event.model import GameEvent, UsersGameEvents
from database import Database

async def get_events():
    db_session = Database.connect_database()

    events = GameEvent.get_events(db_session)

    db_session.close()
    return {
        "status": "ok",
        "events": events
        }