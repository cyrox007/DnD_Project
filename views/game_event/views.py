from components.game_event.model import GameEvent, UsersGameEvents
from database import Database

async def get_events():
    db_session = Database.connect_database()

    events = [
        {
            "id": 1,
            "id_creator": 3,
            "date_event": "2022-05-01",
            "loscut": "Loscut-test",
            "description": "Description",
            "online": False,
            "privacy": True,
            "venue": "Arrd",
            "id_master": None,
            "connected_players_count": 0,
            "game_status": True,
        },
        {
            "id": 2,
            "id_creator": 3,
            "date_event": "2022-05-01",
            "loscut": "Loscut-test",
            "description": "Description",
            "online": False,
            "privacy": True,
            "venue": "Arrd",
            "id_master": "Null",
            "connected_players_count": 0,
            "game_status": True,
        },
        {
            "id": 3,
            "id_creator": 3,
            "date_event": "2022-05-01",
            "loscut": "Loscut-test",
            "description": "Description",
            "online": False,
            "privacy": True,
            "venue": "Arrd",
            "id_master": "Null",
            "connected_players_count": 0,
            "game_status": True,
        },
        {
            "id": 4,
            "id_creator": 3,
            "date_event": "2022-05-01",
            "loscut": "Loscut-test",
            "description": "Description",
            "online": False,
            "privacy": True,
            "venue": "Arrd",
            "id_master": "Null",
            "connected_players_count": 0,
            "game_status": True,
        },
        {
            "id": 5,
            "id_creator": 3,
            "date_event": "2022-05-01",
            "loscut": "Loscut-test",
            "description": "Description",
            "online": False,
            "privacy": True,
            "venue": "Arrd",
            "id_master": "Null",
            "connected_players_count": 0,
            "game_status": True,
        }
    ]

    db_session.close()
    return {
        "status": "ok",
        "events": events
        }