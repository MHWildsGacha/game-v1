import json
import random
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.models import User, Card

router = APIRouter()

def load_cards():
    with open("backend/app/api/cards.json", "r") as file:
        return json.load(file)

def draw_card(cards):
    probabilities = {
        3: 0.8,
        4: 0.15,
        5: 0.05  
    }
    
    rarity_pool = [
        card for card in cards
        if random.random() < probabilities[card["rarity"]]
    ]
    
    if not rarity_pool:
        return draw_card(cards)
    
    return random.choice(rarity_pool)

@router.post("/gacha/{user_id}")
def gacha(user_id: int, num_draws: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    if user.tickets < num_draws:
        raise HTTPException(status_code=400, detail="Not enough tickets")

    cards = load_cards()

    results = []
    for _ in range(num_draws):
        card_data = draw_card(cards)
        results.append({
            "id": card_data["id"],
            "rarity": card_data["rarity"],
            "description": card_data["description"]
        })
        
        card = db.query(Card).filter(Card.id == card_data["id"]).first()
        if not card:
            card = Card(
                id=card_data["id"],
                name=card_data["name"],
                type=card_data["type"],
                rarity=card_data["rarity"],
                attributes=card_data["attributes"],
                description=card_data["description"]
            )
            db.add(card)
        
        user.cards.append(card)

    user.tickets -= num_draws
    db.commit()

    return {"results": results, "remaining_tickets": user.tickets}
