#blackjack game

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

    cardPoints["Ace"] = 0

    for i in range(2, 11):
        cardPoints[i] = i

    for j in specialcards:
        cardPoints[j] = 10

    return cardPoints




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
            
            print(f"Player is betting: £{playerBet}")
                    
            return playerBet, playerMoneyPot




def doubleDownInput(valid_input, playerMoneyPot):
    
    if (playerMoneyPot - (valid_input * 2) <= 0):
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
            
            return valid_input, playerMoneyPot




#DEAL for table
def dealCards(table, playDeck):
    
    for hand in table:
        while len(hand) < 2:
            hand.append(playDeck.pop())

    return table, playDeck





#show the current score and card for player, dealer
def scoreCard(table, tablePoints, pointsDict):
    
    tableList = ["Player", "Dealer"]
    
    for i in range(len(table)):
        scoreCard = table[i].pop(0)
        
        points = pointsDict.get(scoreCard[1])
        
        #changeable value for Ace
        if scoreCard[1] == "Ace":
            if tablePoints[i] + 11 <= 21:
                tablePoints[i] += 11
            else:
                tablePoints[i] += 1
            
        else:
            tablePoints[i] += points
        
        
        print('*' * 10 + '\n')
        print(f'{tableList[i]} Points: {tablePoints[i]}')
        showScoreCards(scoreCard)
         
    return table, tablePoints




def showScoreCards(scoreCard):
    
    #SUITS
    suitDict = {"Hearts": chr(9829), "Diamonds": chr(9830), "Spades": chr(9824), "Clubs": chr(9827)}
    rows = ['', '', '', '', '']
    
    rankDict = {2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9", 10: "10", "Jack": "J", "Queen": "Q", "King": "K", "Ace": "A"}
    
    
    suit, rank = scoreCard
    rows[0] += ' ___ '
    rows[1] += f'|{(rankDict.get(rank)).ljust(2)} | '
    rows[2] += f'| {suitDict.get(suit)} | '
    rows[3] += f'|_{(rankDict.get(rank)).rjust(2)}| '

    for row in rows:
        print(row)




def playerMoveInput():
    
    while True:
        
        try:
            valid_move = (input("Do you want to 'hit' or 'stay'? h/s ")).lower()
            assert(valid_move == "h" or valid_move == "s")
            
        except (AssertionError, ValueError):
            print("Sorry, please enter 'h' (hit) or 's' (stay)")

        else:
            if valid_move == "h":
                return True
            
            else:
                return False




def checkScores(tablePoints):
    
    playerPoints, dealerPoints = tablePoints
        
    if playerPoints >= 21 or dealerPoints >= 21:
        print('Game Over')
        return True
    
    elif dealerPoints >= 17:
        print('Dealer Stays')
        return True
    
    else:
        return False



def playCards(table, tablePoints, playDeck, cardPointsDict):
    
    #deal cards
    table, playDeck = dealCards(table, playDeck)
        
    #add points to player/dealer hand
    #do i add an extra variable here - list display cards to keep track through game of cards?
    table, tablePoints = scoreCard(table, tablePoints, cardPointsDict)
    
    
    return table, tablePoints, playDeck
   
    
    
    
def getMove(table, tablePoints, playDeck, cardPointsDict):
    
    while True:
        check_tableScores = checkScores(tablePoints)
        
        if not check_tableScores:
        
            valid_move = playerMoveInput()
                
            if valid_move:
                                
                table, playDeck = dealCards(table, playDeck)
            
                table, tablePoints = scoreCard(table, tablePoints, cardPointsDict)
            
            else:
                break
           
        else:
            break
    

    return tablePoints




def calculateScore(tablePoints, playerBet, playerMoneyPot):
    
    playerPoints, dealerPoints = tablePoints
    
    if playerPoints == dealerPoints:
        print('Player - Dealer Draw')
    

    elif playerPoints <= 21 and playerPoints > dealerPoints:
        print(f'Player wins: £{playerBet}')
        playerMoneyPot += playerBet
        
        
    else:
        print(f'Player loses: £{playerBet}')
        playerMoneyPot -= playerBet    

    print(f'Player Money Pot remaining: £{playerMoneyPot}')
    
    print('NEWGAME' * 10 + '\n')
    return playerMoneyPot


    

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




def newGameInput(playerMoneyPot):
    
    while True:
        try:
            newGameInput = (input("Do you want to play a new game? y/n")).lower()
            assert(newGameInput == "y" or newGameInput == "n")
    
        except (AssertionError, ValueError):
            print("Sorry, please enter y (yes) or n (no)")
        
        else:
            if newGameInput == "y":
                return True
            
            else:
                return False




def playGame(playerMoneyPot, cardPointsDict):
    
    #create structures to store player/dealer hand, points and playdeck
    (mainTable, mainTablePoints, mainplayDeck) = new_game()
    
    #bet 
    (playerBet, playerMoneyPot) = playerBetInput(playerMoneyPot)

    #start play
    (mainTable, mainTablePoints, mainplayDeck) = playCards(mainTable, mainTablePoints, mainplayDeck, cardPointsDict)
    
    mainTablePoints = getMove(mainTable, mainTablePoints, mainplayDeck, cardPointsDict)
    
    #calculate final points to declare win/draw/lose
    winnings = calculateScore(mainTablePoints, playerBet, playerMoneyPot)
    
    return winnings
    
    



def main():
    
    #player starts with 5000 for main game
    playerMoneyPot = 5000
    
    #stores card point values
    cardPointsDict = createcardPoints()
    
    while playerMoneyPot > 0 and newGameInput(playerMoneyPot):
        playerMoneyPot = playGame(playerMoneyPot, cardPointsDict)
        
        
    return


main()



