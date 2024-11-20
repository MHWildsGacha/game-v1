using JSON

cards_json = "../data/cards.json"

cards = JSON.parsefile(cards_json)

function get_cards()
    return cards
end