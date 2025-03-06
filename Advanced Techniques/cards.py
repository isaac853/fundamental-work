import random 

class Card:
    def __init__(self,givensuit,givenvalue):
        self.suit = givensuit
        self.value = givenvalue

    def displayCard(self):
        symbols = {
            "hearts" : "♥",
            "diamonds" :"♦",
            "clubs" : "♣",
            "spades" : "♠"
        
        }

        #TODO make 10 work as well as kings queens jacks ect
        # have this in one variable, then store in a list to display full hands
        
        card = (f"┌────────────┐\n"
                f"│ {symbols[self.suit]}          │\n"
                f"│            │\n"
                f"│            │\n"
                f"│     {self.value}      │\n"
                f"│            │\n"
                f"│            │\n"
                f"│          {symbols[self.suit]} │\n"
                F"└────────────┘")
        
        
        
        
        
        card10 = (f"┌────────────┐\n│ {symbols[self.suit]}          │\n│            │\n│            │\n│     10     │\n│            │\n│            │\n│          {symbols[self.suit]} │\n└────────────┘")

        if self.value != 10:
            print(card)

        else:
            print(card10)

        print("┌────────────┐")
        print(f"│ {symbols[self.suit]}          │")
        print("│            │")
        print("│            │")
        if self.value != 10:
            print(f"│     {self.value}      │")
        else:
            print((f"│     {self.value}     │"))    
        print("│            │")
        print("│            │")
        print(f"│          {symbols[self.suit]} │")
        print("└────────────┘")


        

class Deck:
    def __init__(self):
        suits = ["hearts","diamonds","spades","clubs"]
        values = ["A",2,3,4,5,6,7,8,9,10,"J","Q","K"]

        self.cards = []

        #give every value to each suit and make a card of each combination
        for suit in suits:
            for value in values:
                self.cards.append(Card(suit,value))
    
    def shuffle(self):
        random.shuffle(self.cards)


    def drawCard(self):
        if len(self.cards) > 0:
            return self.cards.pop()
        
        else:
            print("list is empty")


class Hand(Deck):
    def __init__(self):
        #TODO, this overwrites the attributes of deck, fix that 
        # super().__init__ inherits the above attributes
        self.hand = []

    def draw(self, amount):
        for i in range(amount):
            self.hand.append(self.cards.drawCard())
    
    def viewCards(self):
        for card in self.hand:
            card.displayCard()

# testcard = Card("spades", 1)

# testcard.displayCard()

testDeck = Deck()
testDeck.shuffle()
testDeck.drawCard().displayCard()

testHand = Hand()

testHand.draw(5)
testHand.viewCards