from fastapi import APIRouter, Request, Form, HTTPException, Depends
from typing import List
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.api.gacha import load_cards, draw_card
from app.core.mock_data import mock_user, mock_cards
from fastapi.responses import JSONResponse, HTMLResponse
from app.models.models import Card
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

def serialize_card(card):
    return {
        "id": card.id,
        "name": card.name,
        "type": card.type,
        "rarity": card.rarity,
        "attributes": card.attributes,
        "description": card.description,
    }

@router.get("/mock")
def create_user(db: Session = Depends(get_db)):
    return mock_user(db)

@router.get("/debug/cards")
def get_cards(db: Session = Depends(get_db)):
    cards = db.query(Card).all()
    serialized_cards = [serialize_card(card) for card in cards]
    return JSONResponse(content=serialized_cards)

@router.post("/gacha", response_class=HTMLResponse)
def gacha(request: Request, db: Session = Depends(get_db), draws: int = Form(...)):
    user_id = 1
    results = gacha(db, user_id, draws)
    return templates.TemplateResponse(
        "gacha.html", {"request": request, "results": results}
    )


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
__all__ = ["gacha_router"]
