import random

 # SET UP GLOBALS FOR CARDS
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}

class Card:

    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
    
    def __str__(self):
        return f"{self.rank} of {self.suit}"

class Deck:

    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))
    
    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n' + card.__str__()
        return "The deck has: " + deck_comp

    def length(self):
        return len(self.deck)    
    
    def shuffle(self):
        random.shuffle(self.deck)
    
    def deal(self):
        single_card = self.deck.pop()
        return single_card

class Hand:
    def __init__(self):
        self.cards =[]
        self.value = 0
        self.points = 0

    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]
    
    def clear_hand(self):
        try:
            self.cards.pop() #only removing 1 since we're playing 1 card at a time anyway
            self.value = 0
        except:
            print("No more cards left!")

def hit(deck,hand):
    try:
        single_card = deck.deal()
        hand.add_card(single_card)
    except:
        print("No more cards!")

def show_all(player,dealer):
    print("DEALERS HAND:")
    for card in dealer.cards:
        print(card)
    print("\n")
    print("PLAYERS HAND:")
    for card in player.cards:
        print(card)

def player_wins(player,dealer):
    print("PLAYER WINS!")

def dealer_wins(player,dealer):
    print("DEALER WINS!")

def tie(player,dealer):
    print("TIE!")

# GAME PLAY
while True:
    playing = True
    # Opening statement
    print("Welcome to Card War!")

    # Create/shuffle deck
    deck = Deck()
    deck.shuffle()

    # Deal card to player and dealer
    player_hand = Hand()
    player_hand.add_card(deck.deal())
    
    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())

    while playing:
        show_all(player_hand,dealer_hand)
        if player_hand.value > dealer_hand.value:
            player_wins(player_hand,dealer_hand)
            player_hand.points += 1
        elif player_hand.value == dealer_hand.value:
            tie(player_hand,dealer_hand)
        else:
            dealer_wins(player_hand,dealer_hand)
            dealer_hand.points += 1
        print("\n Player points: " + str(player_hand.points))
        print("\n Dealer points: " + str(dealer_hand.points))
        
        player_hand.clear_hand()
        dealer_hand.clear_hand()

        next_hand = input("Another hand? y/n ")
        if next_hand[0].lower() == 'y':
            hit(deck,player_hand)
            hit(deck,dealer_hand)
        else:
            print("\n Player points: " + str(player_hand.points))
            print("\n Dealer points: " + str(dealer_hand.points))
            playing = False
    if deck.length() == 0 or playing == False:
        new_game = input("\n Would you like to play again? y/n ")

        if new_game[0].lower() == 'y':
            playing = True
            continue
        else:
            print("\n Player points: " + str(player_hand.points))
            print("\n Dealer points: " + str(dealer_hand.points))
            print("Thank you for playing")
            break
    else:
        continue