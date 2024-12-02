from fastapi import FastAPI, Depends, Request, Form
from fastapi.responses import JSONResponse, HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from app.core.database import init_db, get_db, SessionLocal
from app.core.mock_data import mock_user, mock_cards
from app.api.gacha_router import gacha_router
from app.models.models import Card, User


init_db()

app = FastAPI()
templates = Jinja2Templates(directory="app/templates")
@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("base.html", {"request": request})

@app.get("/inventory", response_class=HTMLResponse)
def inventory(request: Request, db: Session = Depends(get_db)):
    user_id = 1
    user = db.query(User).filter(User.id == user_id).first()
    inventory = user.cards if user else []
    return templates.TemplateResponse(
        "inventory.html", {"request": request, "inventory": inventory}
    )

@app.post("/gacha", response_class=HTMLResponse)
def gacha(request: Request, db: Session = Depends(get_db), draws: int = Form(...)):
    user_id = 1
    results = gacha(db, user_id, draws)
    return templates.TemplateResponse(
        "gacha.html", {"request": request, "results": results}
    )

db = SessionLocal()
try:
    mock_user(db) 
    mock_cards(db)
finally:
    db.close()  

app.include_router(gacha_router, prefix="/api")

@app.get("/mock")
def create_user(db: Session = Depends(get_db)):
    return mock_user(db)


def serialize_card(card):
    return {
        "id": card.id,
        "name": card.name,
        "type": card.type,
        "rarity": card.rarity,
        "attributes": card.attributes,
        "description": card.description,
    }


@app.get("/debug/cards")
def get_cards(db: Session = Depends(get_db)):
    cards = db.query(Card).all()
    serialized_cards = [serialize_card(card) for card in cards]
    return JSONResponse(content=serialized_cards)

app.include_router(gacha_router, prefix="/gacha", tags=["Gacha Cards"])