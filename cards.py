from random import randint, shuffle

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    
    def __str__(self):
        return f"{self.suit} {self.rank}"

    def __repr__(self):
        return f"{self.suit} {self.rank}" # Repr skapar en läsbar string om man vill anävnda t.ex print()


class Deck:
    def __init__(self):
        self.cards = Deck.create_deck() # skapar decket 

    @staticmethod
    def create_deck():
        cards = []
        suits = ["♠", "♥", "♣", "♦"]
        ranks = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
        for suit in suits:
            for rank in ranks:
                append_card = Card(suit, rank)
                cards.append(append_card)
        return cards
        

    def deal_cards(self, count):
        dealt_cards = []
        for i in range(count):
            if len(self.cards) > 0:
                dealt_cards.append(self.cards[0])
                self.cards.pop(0)
            else:
                print("No more cards to be dealt")  
                break
        return dealt_cards
            
        
    def shuffle_deck(self):
        shuffle(self.cards)
        print(self.cards)

    def show_deck(self):
        for card in self.cards:
            print(card)
        


def main(): 
    deck = Deck()  # Create a new deck
    print("The deck:")
    deck.show_deck()

    deck.shuffle_deck()  # Shuffle the deck
    print("\nDeck shuffled:")
    deck.show_deck()

    # Deal 5 cards
    dealt_cards = deck.deal_cards(5)
    print("\nYour cards (5 dealt):")
    for card in dealt_cards:
        print(card)

    print("\nCards left in the deck:")
    deck.show_deck()
    

if __name__ == "__main__":
    main()