import json
from fastapi import FastAPI, HTTPException

app = FastAPI()

card_file = "/home/herei/code/MHGacha/backend/services/cards-service/data/cards.json"

def load_cards():
    with open(card_file, 'r') as file:
        return json.load(file)

@app.get("/cards")
def get_cards():
    cards = load_cards()  
    return cards

@app.get("/cards/{card_id}")
def get_card_by_id(card_id: int):
    cards = load_cards()
    for card in cards: 
        if card["id"] == card_id:
            return card
    raise HTTPException(status_code=404, detail="Card not found")

@app.get("/")
def main():
    return {"message": "API funcionando!"}
