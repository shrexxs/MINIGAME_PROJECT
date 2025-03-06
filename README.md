# PYTHON_MINIGAME_PROJECT
# Card Game Simulation and Analysis
# Card Game Framework

## Problem Statement
Design and implement a basic card game framework that supports simple card games like **Blackjack**. The framework should include a deck of cards, players, and basic game rules. The goal of this project is to create an extendable and reusable structure that can accommodate different card games by implementing fundamental components such as a deck of cards, a hand, and a set of game rules. 

For example, in Blackjack, the objective is to achieve a hand value as close to 21 as possible without exceeding it. The game involves a dealer and one or more players. The dealer follows fixed rules for drawing cards, while players can decide whether to draw additional cards.

## Tasks

### 2.1 Task 1: Create Card and Deck Classes
- **Card Class:** 
  - Represents a single playing card.
  - Each card should have a suit (Hearts, Diamonds, Clubs, or Spades) and a rank (Ace, 2, 3, ..., 10, Jack, Queen, King).
  - Use an enum type to define suits, ensuring consistency and preventing errors due to typos.

- **Deck Class:**
  - Generates a full deck of 52 cards, consisting of four suits and thirteen ranks each.
  - Adds functionality to shuffle the deck randomly.
  - Implements a method to draw a card from the deck, removing it from the available cards.

- **Example Data:**
  - Example of a single card: `Card(suit=Hearts, rank=Ace)`.
  - Example of a shuffled deck: `[Card(Spades, King), Card(Diamonds, 7), Card(Hearts, 2), ...]`.

### 2.2 Task 2: Implement a Simple Blackjack Game
- Objective: Players aim to get as close to 21 points as possible without exceeding it. 
  - Face cards (King, Queen, Jack) are worth 10 points.
  - Aces can be worth 1 or 11 points, and other cards retain their numeric values.
  
- Game Flow:
  - The dealer and the player are dealt two cards at the start of the game.
  - Players can decide to **hit** (draw an additional card) or **stand** (don’t take any more cards).
  - If a player’s total exceeds 21, they bust and lose the game.

- Dealer Rules:
  - Must hit if their total is 16 or below.
  - Must stand on 17 or above.

- Winning Condition:
  - A player wins if their total is higher than the dealer's without exceeding 21.

- **Example Scenario:**
  - Player’s Hand: `[Card(Hearts, 10), Card(Clubs, 7)]` Total: 17
  - Dealer’s Hand: `[Card(Spades, 8), Card(Diamonds, 10)]` Total: 18
  - Result: Dealer wins.

### 2.3 Task 3: Implement Multiplayer Support
- Extend the framework to support multiple players in a game.
- Allow each player to take turns making decisions (e.g., hit or stand in Blackjack).
- Implement a turn-based system to manage player actions and game progression.
- Display player hands and game status after each round.

- **Example Data:**
  - Player 1 Hand: `[Card(Hearts, 7), Card(Spades, 5)]`
  - Player 2 Hand: `[Card(Diamonds, 9), Card(Clubs, 6)]`
  - Player 1 hits and receives `Card(Hearts, 3)`.
  - Updated Hand: `[Card(Hearts, 7), Card(Spades, 5), Card(Hearts, 3)]` (Total = 15).

## Basic Rules of the Game
- The goal is to get as close to 21 as possible without going over.
- Face cards (King, Queen, Jack) are valued at 10 points.
- Aces (A) can be valued at either 1 or 11, depending on what benefits the player.
- If a player’s total is higher than the dealer’s without busting (going over 21), they win.
- If a player goes over 21, they automatically lose.
- The dealer must hit if they have 16 or less and stand on 17 or more.

## When Does a Blackjack Game End?
A game of Blackjack concludes in the following scenarios:

- **Immediate Loss: Player Busts**
  - If a player’s total exceeds 21, they lose automatically.
  - Other players continue until they either bust or stand.

- **Immediate Win: Dealer Busts**
  - If the dealer’s total exceeds 21, all remaining players who have not busted automatically

 
