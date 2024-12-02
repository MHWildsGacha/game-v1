from fastapi import FastAPI, Depends, Request
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session
from app.core.database import init_db, get_db, SessionLocal
from app.api.gacha_router import gacha_router
from app.models.models import User
from app.core.mock_data import mock_user, mock_cards
from fastapi.templating import Jinja2Templates


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

db = SessionLocal()
try:
    mock_user(db) 
    mock_cards(db)
finally:
    db.close()  

app.include_router(gacha_router, prefix="/api")
app.include_router(gacha_router)