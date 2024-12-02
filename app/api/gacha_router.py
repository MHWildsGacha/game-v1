from fastapi import APIRouter, HTTPException, Depends
from typing import List
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.api.gacha import load_cards, draw_card

router = APIRouter()

@router.get("/cards", response_model=List[dict])
async def get_all_cards():
    cards = load_cards()
    return cards

@router.get("/cards/{card_id}", response_model=dict)
async def get_card(card_id: int):
    cards = load_cards()
    for card in cards:
        if card["id"] == card_id:
            return card
    raise HTTPException(status_code=404, detail="Card not found")

@router.get("/gacha", response_model=dict)
async def get_random_card(db: Session = Depends(get_db)):
    cards = load_cards()
    drawn_card = draw_card(cards)
    return {
        "id": drawn_card["id"],
        "rarity": drawn_card["rarity"],
        "description": drawn_card["description"]
    }

gacha_router = APIRouter()
gacha_router.include_router(router, prefix="/gacha")
