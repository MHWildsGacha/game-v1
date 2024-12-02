from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from app.core.database import init_db, get_db, SessionLocal
from app.api.gacha_router import gacha_router
from app.core.mock_data import mock_user, mock_cards
from fastapi.templating import Jinja2Templates


init_db()

app = FastAPI()
templates = Jinja2Templates(directory="app/templates")
@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("base.html", {"request": request})



db = SessionLocal()
try:
    mock_user(db) 
    mock_cards(db)
finally:
    db.close()  

app.include_router(gacha_router, prefix="/api")
app.include_router(gacha_router)