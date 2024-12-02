from sqlalchemy.orm import Session
from app.models.models import User, Card
from app.core.database import get_db

def mock_user(db: Session):
    user_id = 1
    user = db.query(User).filter_by(id=user_id).first()
    if not user:
        new_user = User(id=user_id, tickets=20)
        db.add(new_user)
        db.commit()
        db.refresh(new_user)  
    return user

def mock_cards(db: Session):
    card_data = [
        {"name": "Rathalos", "type": "Monster", "rarity": 5, "description": "A fearsome fire-breathing wyvern."},
        {"name": "Hunter A", "type": "Human", "rarity": 4, "description": "A skilled hunter from the guild."},
        {"name": "Felyne Chef", "type": "Palico", "rarity": 3, "description": "A culinary expert Palico."}
    ]
    for card in card_data:
        exists = db.query(Card).filter_by(name=card["name"]).first()
        if not exists:
            new_card = Card(**card)
            db.add(new_card)
    db.commit()