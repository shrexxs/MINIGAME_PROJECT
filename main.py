#Card GameSimulation and Analysis

from enum import Enum
import random
from typing import List, Optional

class CardSuit(Enum):
    HEART = "Heart"
    DIAMOND = "Diamond"
    CLUB = "Club"
    SPADE = "Spade"

class PlayingCard:
    def __init__(self, suit: CardSuit, value: str):
        self.suit = suit
        self.value = value
    
    def __repr__(self) -> str:
        return f"Card({self.suit.value}, {self.value})"
    
    def get_numeric_value(self) -> int:
        if self.value in ["Jack", "Queen", "King"]:
            return 10
        elif self.value == "Ace":
            return 11
        else:
            return int(self.value)

class CardDeck:
    def __init__(self):
        self.cards = []
        self.create_fresh_deck()
    
    def create_fresh_deck(self):
        card_values = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
        self.cards = []
        
        for suit in CardSuit:
            for value in card_values:
                self.cards.append(PlayingCard(suit, value))
    
    def shuffle_deck(self):
        random.shuffle(self.cards)
    
    def deal_card(self) -> Optional[PlayingCard]:
        if len(self.cards) == 0:
            print("Warning: No cards left in the deck")
            return None
        return self.cards.pop()
    
    def cards_remaining(self) -> int:
        return len(self.cards)

class CardHand:
    def __init__(self):
        self.cards = []
    
    def add_card(self, card: PlayingCard):
        if card:
            self.cards.append(card)
    
    def calculate_value(self) -> int:
        total_value = 0
        ace_count = 0
        
        for card in self.cards:
            card_value = card.get_numeric_value()
            total_value += card_value
            
            if card.value == "Ace":
                ace_count += 1
        
        while total_value > 21 and ace_count > 0:
            total_value -= 10  # Convert one Ace from 11 to 1
            ace_count -= 1
            
        return total_value
    
    def is_busted(self) -> bool:
        return self.calculate_value() > 21
    
    def __str__(self) -> str:
        card_list = ", ".join(repr(card) for card in self.cards)
        return f"[{card_list}] (Total: {self.calculate_value()})"


class GameParticipant:
    def __init__(self, name: str):
        self.name = name
        self.hand = CardHand()
        self.has_stood = False
        self.has_busted = False
    
    def receive_card(self, card: PlayingCard):
        
        self.hand.add_card(card)
        if self.hand.is_busted():
            self.has_busted = True
    
    def choose_stand(self):
        self.has_stood = True
    
    def can_take_action(self) -> bool:
        return not (self.has_stood or self.has_busted)
    
    def reset_for_new_game(self):
        self.hand = CardHand()
        self.has_stood = False
        self.has_busted = False

class BlackjackDealer(GameParticipant):
    def __init__(self):
        super().__init__("Dealer")
    
    def play_by_rules(self, deck: CardDeck):
        print(f"\n{self.name} reveals full hand: {self.hand}")
        
        while self.hand.calculate_value() < 17 and not self.has_busted:
            card = deck.deal_card()
            if card:
                print(f"{self.name} draws: {card}")
                self.receive_card(card)
                print(f"{self.name}'s hand: {self.hand}")
            else:
                print("No more cards available.")
                break
        
        if self.has_busted:
            print(f"{self.name} busts with {self.hand.calculate_value()}!")
        else:
            self.choose_stand()
            print(f"{self.name} stands with {self.hand.calculate_value()}.")


class BlackjackPlayer(GameParticipant):
    def __init__(self, name: str):
        super().__init__(name)

class BlackjackGameManager:
    def __init__(self, player_names: List[str]):
        self.deck = CardDeck()
        self.players = [BlackjackPlayer(name) for name in player_names]
        self.dealer = BlackjackDealer()
    
    def deal_initial_cards(self):
        for _ in range(2):
            for player in self.players:
                player.receive_card(self.deck.deal_card())
            self.dealer.receive_card(self.deck.deal_card())
    
    def show_initial_game_state(self):
        dealer_first_card = self.dealer.hand.cards[0]
        print(f"Dealer shows: {dealer_first_card}")
        for player in self.players:
            print(f"{player.name}'s hand: {player.hand}")
    
    def handle_player_turns(self):
        for player in self.players:
            self.handle_single_player_turn(player)
    
    def handle_single_player_turn(self, player: BlackjackPlayer):
        print(f"\n--- {player.name}'s Turn ---")
        while player.can_take_action():
            print(f"{player.name}'s hand: {player.hand}")
            choice = input(f"{player.name}, do you want to hit or stand? ").lower().strip()
            
            if choice == 'h':
                card = self.deck.deal_card()
                if card:
                    print(f"{player.name} receives: {card}")
                    player.receive_card(card)
                    
                    if player.has_busted:
                        print(f"{player.name} busts with {player.hand.calculate_value()}!")
                        break
                else:
                    print("No more cards in the deck!")
                    break
            elif choice == 's':
                player.choose_stand()
                print(f"{player.name} stands with {player.hand.calculate_value()}.")
                break
            else:
                print("Invalid choice. Please enter 'h' for hit or 's' for stand.")
    
    def handle_dealer_turn(self):
        active_players = [p for p in self.players if not p.has_busted]
        
        if active_players:
            self.dealer.play_by_rules(self.deck)
    
    def determine_results(self):
        dealer_value = self.dealer.hand.calculate_value()
        dealer_busted = self.dealer.has_busted
        
        print("\nGame Results => ")
        
        for player in self.players:
            player_value = player.hand.calculate_value()
            
            if player.has_busted:
                result = "LOSS (busted)"
            elif dealer_busted:
                result = "WIN (dealer busted)"
            elif player_value > dealer_value:
                result = "WIN"
            elif player_value < dealer_value:
                result = "LOSS"
            else:
                result = "PUSH (tie)"
            
            print(f"{player.name}: {result} - Hand: {player.hand}")
        
        print(f"Dealer's final hand: {self.dealer.hand}")
    
    def prepare_new_game(self):
        self.deck = CardDeck()
        self.deck.shuffle_deck()
        
        for player in self.players:
            player.reset_for_new_game()
        
        self.dealer.reset_for_new_game()
    
    def run_game(self):
        self.prepare_new_game()
        self.deal_initial_cards()
        self.show_initial_game_state()
        self.handle_player_turns()
        self.handle_dealer_turn()
        self.determine_results()
        return input("\nPlay another round? (y/n): ").lower().strip() == 'y'


def main():
    print("Welcome to Blackjack!")
    
    while True:
        try:
            num_players = int(input("Enter number of players (1-7): "))
            if 1 <= num_players <= 7:
                break
            else:
                print("Please enter a number between 1 and 7.")
        except ValueError:
            print("Please enter a valid number.")
    
    player_names = []
    for i in range(num_players):
        name = input(f"Enter name for Player {i+1}: ")
        player_names.append(name or f"Player {i+1}")
    
    game_manager = BlackjackGameManager(player_names)
    play_again = True
    while play_again:
        play_again = game_manager.run_game()
    
    print("Thank you for playing!")


if __name__ == "__main__":
    main()
