# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 949x392 - source: jfitz.com
CARD_SIZE = (73, 98)
CARD_CENTER = (36.5, 49)
card_images = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/cards.jfitz.png")

CARD_BACK_SIZE = (71, 96)
CARD_BACK_CENTER = (35.5, 48)
card_back = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/card_back.png")    

# initialize some useful global variables
in_play = False
message = ""
outcome = ""
score = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        # create Hand object
        self.hand = []

    def __str__(self):
        # return a string representation of a hand
        hand_in_string = ""
        for card in self.hand:
            hand_in_string += str(card) + " "
            
        return "Hand contains " + hand_in_string

    def add_card(self, card):
        # add a card object to a hand
        self.hand += [card]

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        # compute the value of the hand, see Blackjack video
        count = 0
        ace = False
        for card in self.hand:
            rank = card.get_rank()
            count += VALUES[rank]
            if rank == 'A':
                ace = True
        if ace and (count + 10 <=21):
            count += 10
        return count
   
    def draw(self, canvas, pos):
        # draw a hand on the canvas, use the draw method for cards
        for card in self.hand:
            card.draw(canvas, pos)
            pos[0] += CARD_SIZE[0] + 20
        
# define deck class 
class Deck:
    def __init__(self):
        # create a Deck object
        self.deck = []
        for suit in SUITS:
            for rank in RANKS:
                card = Card(suit, rank)
                self.deck.append(card)

    def shuffle(self):
        # shuffle the deck 
        # use random.shuffle()
        random.shuffle(self.deck)

    def deal_card(self):
        # deal a card object from the deck
        return self.deck.pop(0)
    
    def __str__(self):
        # return a string representing the deck
        deck_in_string = ""
        for card in self.deck:
            deck_in_string += str(card) + " "
        return "Deck contains " + deck_in_string 

#define event handlers for buttons
def deal():
    global outcome, in_play, deck, player, dealer, game, message, outcome, in_play, score
    
    if message == "Hit or stand?":
        score -= 1
    # your code goes here
    deck = Deck()
    deck.shuffle()
    player = Hand()
    dealer = Hand()
    game = True
    message = "Hit or stand?"
    outcome = ""
    in_play = True
    for i in range(2):
        player.add_card(deck.deal_card())
        dealer.add_card(deck.deal_card())
    
def hit():
    # replace with your code below
    global player, game, message, outcome, in_play, score
    if game:
        # if the hand is in play, hit the player
        player_hand_value = player.get_value() 
        if player_hand_value < 21:
            player.add_card(deck.deal_card())
            player_hand_value = player.get_value()
            if player_hand_value > 21:
                game = False
                outcome = "You have busted!"
                message = "New deal?"
                in_play = False
                score -= 1
        # if busted, assign a message to outcome, update in_play and score
    
def stand():
    # replace with your code below
    global dealer, game, message, outcome, in_play, score
    
    if game:
        dealer_hand_value = dealer.get_value()
        while dealer_hand_value < 17:
            dealer.add_card(deck.deal_card())
            dealer_hand_value = dealer.get_value()
        if dealer_hand_value > 21:
            outcome = "Dealer has busted!"
            score += 1
        else:
            player_hand_value = player.get_value()
            if player_hand_value <= dealer_hand_value:
                score -= 1
                outcome = "Dealer wins!"
            else:
                score += 1
                outcome = "Player wins!"
                
    game = False
    in_play = False
    message = "New deal?"
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more

    # assign a message to outcome, update in_play and score
    
# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    
    dealer.draw(canvas, [50, 150])
    color_palette = ["Red", "Blue", "Yellow", "Orange", "White", "Purple", "Black"]
    if in_play:
        canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, [86, 199], CARD_BACK_SIZE)  
    player.draw(canvas, [50, 450])
    canvas.draw_text("Blackjack!", [150, 50], 45, "Cyan")
    canvas.draw_text("Dealer", [75, 125], 30, "Black")
    canvas.draw_text("Player", [75, 425], 30, "Black")
    canvas.draw_text(message, [250, 425], 30, "Purple")
    if outcome == "Player wins!":
        canvas.draw_text(outcome, [200, 125], 30, color_palette[random.randrange(0, len(color_palette))])
    else:
        canvas.draw_text(outcome, [200, 125], 30, "White")
    canvas.draw_text("Score: " + str(score), [450, 100], 30, "Black")

# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()


# remember to review the gradic rubric