#blackjack game

#dealer / player - interaction
#shared deck of cards per round
#try to get as close to 21 without going over
#hit to take a card
#stay to stop taking cards
#when both dealer and player stay --> end round
#show cards

#RUNNING A GAME
#player starts with 5000
#place a bet at start of game
#once cards been dealt you can double down,
#that requires you to hit one more time
#if you win --> win bet money
#if you lose --> lose bet
#if you doubledown --> win bet money * 2
#if you have no money to make bet, out game


import random


#MONEY
#player starts with 5000 per game
playerMoneyPot = 5000

#SUITS
hearts = chr(9829)
diamonds = chr(9830)
spades = chr(9824)
clubs = chr(9827)


#create a deck 
def createDeck():
    new_deck = []
    allcardsTemplate = []
    
    suitTemplate = ["Hearts", "Diamonds", "Spades", "Clubs"]
    specialcardsTemplate = ["Jack", "Queen", "King", "Ace"]

    for i in range(2, 11):
        allcardsTemplate.append(i)

    allcardsTemplate.extend(specialcardsTemplate)

    for i in suitTemplate:
        for j in allcardsTemplate:
            new_deck.append((i, j))
    
    for i in range(3):
        random.shuffle(new_deck)
    
    return new_deck

playDeck = createDeck()



#need a function that iterates over the playdeck to pull out points value and match it to dictionary value
#need to create a dictionary storing all values for cards

def createcardPoints():
    cardPoints = {}
    specialcards = ["Jack", "Queen", "King"]
    ace_card = [1, 11]

    for i in range(2, 11):
        cardPoints[i] = i

    for j in specialcards:
        cardPoints[j] = 10

    cardPoints["Ace"] = ace_card
    
    return cardPoints

testpoints = createcardPoints()



playerHand = []
dealerHand = []
playerpoints = 0
dealerpoints = 0

#DEAL
#for both player and dealer
def dealCards(playerHand, dealerHand, playDeck):
    
    table = [playerHand, dealerHand]
    
    for hand in table:
        
        while len(hand) < 2:
            hand.append(playDeck.pop())

    
    return playerHand, dealerHand, playDeck

dealCards(playerHand, dealerHand, playDeck)


#add points from hand to player/dealer total

def scoreCard(playerHand, dealerHand, playerpoints, dealerpoints):
    #check length of hand is 2, if not add a card
    pass

    #score top card in player/dealer hand to player/dealer points

    #show top card in player/dealer hand
    

    pass


#show 1 card from hand





#score points for card in hand in ("suit", "card point value")
#testcards = [("hearts", 5)]



#BETTING
#check is the player money > 0
#ask player how much to bet per round
#store bet value per game
#if the player wins the round
    #check if double down is true/false
        #if dd is true, add double bet money value to player money total 
        #else add bet value to the player money total 
#if the player loses the round
    #check if double down is true/false
        #if dd is false, subtract double bet money value to player money total 
        #else subtract bet value to the player money total 
#if the dealer/player draw
    #no change to value of player money total


#PLAY GAME
#new deck created 
#create empy totals for player/dealer
#create card pile fo player/dealer

#put two cards on each pile
#show one card card[0]
#show card face up/one card face down for player/dealer in illustration
    #add points to player/dealer total
#ask player if they want to double down
    #if yes, doubledown = true

#NEW DEAL
#does the player want to play or stay

    #if player wants to play
        #ask player if they want to play a card
            #if yes, reveal card[1] in card pile
            #add points to player total
            #create new deal
            
        #if dealer total < 17, dealer plays a card
            #if yes, reveal card[1] in card pile
            #add points to dealer total
            #create new deal

    #if player wants to stay
        #check dealer is < 17
            #if yes dealer only plays
            #if no calculate points


#CALCULATE POINTS
#compare player/dealer total
    #if player wins
        #return win
    #if player draws
        #return draw
    #if player loses
        #return lose    



