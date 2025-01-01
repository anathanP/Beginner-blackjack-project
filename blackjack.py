import project_resource as pr
import os
from random import choice


def clear() -> None:
    """Clears the terminal"""
    os.system("cls" if os.name=="nt" else "clear")

def draw_card() -> str:
    """Draws a card"""
    return choice(list(pr.cards.keys()))

def score(cards: list) -> int:
    """Gets a set of blackjack cards and return the score"""
    total_score = 0
    ace_count = 0
    for card in cards:
        if card == "Ace":
            ace_count += 1
        else:
            total_score += pr.cards[card]
    if ace_count == 0:
        return total_score
    
    remaining_score = pr.threshold - total_score
    for ace in range(ace_count):
        if remaining_score >= max(pr.cards["Ace"]):
            total_score += max(pr.cards["Ace"])
        else:
            total_score += min(pr.cards["Ace"])
    return total_score

def game_log(player_cards: list, dealer_cards: list, full: bool=False) -> None:
    print(f"Your cards: {player_cards} current score is : {score(player_cards)}")
    if full:
        print(f"Computer cards are : {dealer_cards} computer score is : {score(dealer_cards)}")
    else:    
        print(f"Computer cards are : {dealer_cards[0:len(dealer_cards)-1]} computer score is : {score(dealer_cards[0:len(dealer_cards)-1])}")

def call(player_cards: list, dealer_cards: list) -> str:
    player = score(player_cards)
    dealer = score(dealer_cards)
    if player > 21:
        return "Lost"
    if dealer > 21:
        return "Won"
    if dealer == player:
        return "Draw"
    if player < dealer:
        return "Lost"
    return "Won"

def end_game(player_cards: list, dealer_cards: list) -> None:
    while score(dealer_cards) < 17:
        dealer_cards.append(draw_card())
    game_log(player_cards, dealer_cards, True)
    print(f"You {call(player_cards, dealer_cards)}")

def blackjack() -> None:
    """Start the blackjack game"""
    
    print(pr.logo)
    
    dealer_cards = [draw_card(), draw_card()]
    player_cards = [draw_card(), draw_card()]
    
    game_log(player_cards, dealer_cards)
    
    redraw = input("Type 'y' to draw another card or 'n' to pass.\n").lower()
    while redraw == "y":
        player_cards.append(draw_card())
        game_log(player_cards, dealer_cards)
        if score(player_cards) > 21:
            end_game(player_cards, dealer_cards)
            break
        redraw = input("Type 'y' to draw another card or 'n' to pass.\n").lower()    
    end_game(player_cards, dealer_cards)        
