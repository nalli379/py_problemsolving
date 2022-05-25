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



#dictionary to store/retrieve points value for card deck
def createcardPoints():
    cardPoints = {}
    specialcards = ["Jack", "Queen", "King"]
    ace_card = 0

    cardPoints["Ace"] = 0

    for i in range(2, 11):
        cardPoints[i] = i

    for j in specialcards:
        cardPoints[j] = 10

    return cardPoints



#DEAL for table
def dealCards(table, playDeck):
    
    for hand in table:
        while len(hand) < 2:
            hand.append(playDeck.pop())

    return table, playDeck



#score card FIFO order for table
def scoreCard(table, tablePoints, pointsDict):
    
    for i in range(len(table)):
        scoreCard = table[i].pop(0)
        
        points = pointsDict.get(scoreCard[1])
        
        if scoreCard[i] == 'Ace':
            if tablePoints[i] + 11 <= 21:
                tablePoints[i] += 11
            else:
                tablePoints[i] += 1
            
        else:
            tablePoints[i] += points
    
    return table, tablePoints



#SHOW card FIFO order for table --> need to sort input (dealt cards)
def showCards(table):
    
    #SUITS
    hearts = chr(9829)
    diamonds = chr(9830)
    spades = chr(9824)
    clubs = chr(9827)
    
    player, dealer = table
    
    return None
  
# test = [[('Spades', 'Ace')], [('Clubs', 2)]]
# showCards(test)


def doubleDownInput(valid_input, playerMoneyPot):
    
    if (playerMoneyPot - (valid_input * 2) <= 0):
        print('here')
        return valid_input, playerMoneyPot
    
    while True:
        
        try:
            valid_bet = (input("Do you want to double your bet? y/n ")).lower()
            assert(valid_bet == "y" or valid_bet == "n")
            
        except (AssertionError, ValueError):
            print("Sorry, please enter y (yes) or n (no)")

        else:
            
            if valid_bet == "y":
                valid_input *= 2
         
            playerMoneyPot -= valid_input
            
            
            return valid_input, playerMoneyPot



def playerBetInput(playerMoneyPot):
    
    if playerMoneyPot <= 0:
        return 0

        
    while True:
        
        try:
            valid_input = int((input("How much do you want to bet? ")))
            assert(playerMoneyPot - valid_input >= 0 and valid_input > 0)
            
        except (AssertionError, ValueError):
            print("Sorry, please enter a number between 1 - 5000")

        else:
            
            playerBet, playerMoneyPot = doubleDownInput(valid_input, playerMoneyPot)
            
            
            playerMoneyPot -= valid_input              
            return valid_input, playerMoneyPot








#EXECUTION 
def new_game():
    
    playerHand = []
    dealerHand = []
    playerpoints = 0
    dealerpoints = 0

    #data structures for player/dealer for hand/points
    table = [playerHand, dealerHand]
    tablePoints = [playerpoints, dealerpoints]
    
    #create a new deck
    playDeck = createDeck()
    
    return (table, tablePoints, playDeck)



def playCards(table, tablePoints, playDeck, cardPointsDict):
    
    #deal cards
    table, playDeck = dealCards(table, playDeck)
        
    #add points to player/dealer hand
    table, tablePoints = scoreCard(table, tablePoints, cardPointsDict)
    
    return table, tablePoints, playDeck



def main():
    
    #dict stores card point values
    cardPointsDict = createcardPoints()

    #player starts with 5000 for main game
    playerMoneyPot = 5000
    
    (mainTable, mainTablePoints, mainplayDeck) = new_game()
    
    #bet 
    (playerBet, playerMoneyPot) = playerBetInput(playerMoneyPot)
    

    (mainTable, mainTablePoints, mainplayDeck) = playCards(mainTable, mainTablePoints, mainplayDeck, cardPointsDict)
    
    
    return 0


# main()



#BETTING

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



