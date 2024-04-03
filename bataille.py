import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten',
         'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8,
          'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

class Card():
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
    def __str__(self):
        return f"The card is a {self.rank} of {self.suit}"

class Deck:
    def __init__(self):
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                myCard = Card(suit, rank)
                self.all_cards.append(myCard)
    def shuffle_card(self):
        random.shuffle(self.all_cards)
        print("The deck has been shuffled")
    
    def deal_one(self):
        try:
            return self.all_cards.pop()
        except:
            print("There is no more cards in your deck !")
        

class Player:
    def __init__(self, name):
        self.name = name
        self.all_cards = []
    
    def remove_one(self):
        return self.all_cards.pop(0)
    
    def add_cards(self, new_cards):
        return self.all_cards.extend(new_cards)
        
    def __str__(self):
        return f"The player name is {self.name} and it has {len(self.all_cards)} cards in hands."
        
#game setup
player1 = Player("John")
player2 = Player("Lizbeth")

new_deck = Deck()
new_deck.shuffle_card()


#split game in half (always 52 cards in a deck)
player1.add_cards(new_deck.all_cards[0:26])
player2.add_cards(new_deck.all_cards[26:52])

game_on = True


round_num = 0

while game_on:
    at_war = True

    
    if len(player1.all_cards) == 0:
        print("Player 2 won the game!")
        game_on = False
        break
        
    elif len(player2.all_cards) == 0:
        print("Player 1 won the game!")
        game_on = False
        break

    #Starting a new round

    round_num += 1
    print(f"Round {round_num}")
    
    player1_cards = []
    player2_cards = []
    
    player1_cards.append(player1.remove_one())
    player2_cards.append(player2.remove_one())
    

      
    while at_war:
        print("Here is player 1")
        for card in player1_cards:
            print(card)
        
        print("Here is player 2")
        for card in player2_cards:
            print(card)
            
        if player1_cards[-1].value < player2_cards[-1].value:
            player2.add_cards(player1_cards)
            player2.add_cards(player2_cards)
            print("Player 2 won the round !\n")
            at_war = False
            break

            
        elif player1_cards[-1].value > player2_cards[-1].value:
            player1.add_cards(player1_cards)
            player1.add_cards(player2_cards)
            print("Player 1 won the round !\n")
            at_war = False
            break
            
        else:
            for i in range(30):
                try:
                    player1_cards.append(player1.remove_one())
                    player2_cards.append(player2.remove_one())
                except:
                    break
