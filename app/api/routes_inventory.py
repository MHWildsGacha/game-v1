from app.models.models import User
from fastapi import Depends, Request, APIRouter
from sqlalchemy.orm import Session
from app.core.database import get_db
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
router = APIRouter()

templates = Jinja2Templates(directory="app/templates")

@router.get("/inventory", response_class=HTMLResponse)
def inventory(request: Request, db: Session = Depends(get_db)):
    user_id = 1
    user = db.query(User).filter(User.id == user_id).first()
    inventory = user.cards if user else []
    return templates.TemplateResponse(
        "inventory.html", {"request": request, "inventory": inventory}
    )