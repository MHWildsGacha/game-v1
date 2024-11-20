import json
from fastapi import FastAPI

app = FastAPI() 

card_file = "/home/herei/code/MHGacha/backend/services/cards-service/data/cards.json"

def load_cards():
    with open(card_file, 'r') as file:
        return json.load(file)

@app.get("/cards")
def get_cards():
    cards = load_cards
    return cards

@app.get("/")
def main():
    print("api funciona")
main()