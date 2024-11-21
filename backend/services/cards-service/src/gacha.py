import json
import random
from api import card_file

def load_cards():
    with open(card_file, 'r') as file:
        return json.load(file)

def gacha_cards(cards):
    ssr_cards = [card for card in cards if card['rarity'] == 'SSR']
    normal_cards = [card for card in cards if card['rarity'] != 'SSR']

    if random.random() < 0.01:  #Não sou bom em matematica, mas acho que a chance é 0.01%
        prize = random.choice(ssr_cards)
        print("SSR!")
    else:  
        prize = random.choice(normal_cards)
        print(f"rodou um rare {prize['rarity']} "),

def main():
    cards = load_cards()
    gacha_cards(cards)

if __name__ == "__main__":
    main()
