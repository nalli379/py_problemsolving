import random

#parent class for player, dealer for shared methods
class tableHand ():
    def __init__(self):
        self.hand = []
        self.points = 0
        self.name = None
    
    
    def newDeal(self, cards):
        self.newcards = cards
        self.hand.extend(self.newcards)
        return self.hand
    

    def hit(self, card):
        self.newcard = card
        self.hand.append(self.newcard)
        return self.hand
    
    
    def reset(self):
        self.hand = []
        self.points = 0
        
    
    def calculatePoints(self, cardPointsDict):
        
        self.points = 0
        
        for card in self.hand:
            self.scoreCard = card[1]    
            self.cardPointsvalue = cardPointsDict.get(self.scoreCard)
            
            if self.scoreCard == "Ace":
                if self.points + 11 <= 21:
                    self.points += 11
                else:
                    self.points += 1
            
            else:
                self.points += self.cardPointsvalue
        
        return self.points



    def showHand(self):

        rows = ['', '', '', '', '']
        
        for i, card in enumerate(self.hand):
            suitDict = {"Hearts": chr(9829), "Diamonds": chr(9830), "Spades": chr(9824), "Clubs": chr(9827)}
            
            rankDict = {2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9", 10: "10", "Jack": "J", "Queen": "Q", "King": "K", "Ace": "A"}
            
            
            suit, rank = card
            rows[0] += ' ___ '
            rows[1] += f'|{(rankDict.get(rank)).ljust(2)} | '
            rows[2] += f'| {suitDict.get(suit)} | '
            rows[3] += f'|_{(rankDict.get(rank)).rjust(2)}| '

            for row in rows:
                print(row)
    

    def __str__(self):
        return f"{self.name}: {self.points} points"

#dealer can hit up to 17 points
class Dealer(tableHand):
    
    def __init__(self):
        super().__init__()
        self.name = "Dealer"
        
    
    def hit(self, card):
        if self.points >= 17:
            print('Dealer Stays')
            
        else:
            self.newcard = card
            self.hand.append(self.newcard)
        
        return self.hand


#player has money pot and methods to check betting is valid, won/lost
class Player(tableHand):
    def __init__(self):
        super().__init__()
        self.name = "Player"
        self.moneypot = 5000
        

    def checkBet(self, bet):
        if self.moneypot - bet < 0:
            return False
        else:
            return True
    
    def winBet(self, bet):
        self.moneypot += bet
        return self.moneypot
    
    def loseBet(self, bet):
        self.moneypot -= bet
        return self.moneypot
 
    
#creates new deck of cards 
class cardDeck():
    def __init__(self):
        self.newDeck = []
        self.allcards = []
        self.suit = ["Hearts", "Diamonds", "Spades", "Clubs"]
        self.specialcards = ["Jack", "Queen", "King", "Ace"]
        
        for i in range(2, 11):
            self.allcards.append(i)
        
        self.allcards.extend(self.specialcards)
        
        for i in self.suit:
            for j in self.allcards:
                self.newDeck.append((i, j))
        
        for i in range(3):
            random.shuffle(self.newDeck)


    def dealCards(self):
        self.deal = []
        for i in range(2):
            self.deal.append(self.newDeck.pop())
        return self.deal
    
    
    def pop(self):
        return self.newDeck.pop()
    
    def __str__(self):
        return str(self.newDeck)


#creates points values reference for cards
class cardPoints():
    
    def __init__(self):
        self.cardPoints = {}
        self.cardPoints["Ace"] = 0
        self.specialcards = ["Jack", "Queen", "King"]
        
        for i in range(2, 11):
            self.cardPoints[i] = i
        
        for j in self.specialcards:
            self.cardPoints[j] = 10

        
    def get(self, cardvalue):
        return self.cardPoints.get(cardvalue)
    
    def __str__(self):
        return str(self.cardPoints)


#scores game play awarding/subtracting bet money per game, resetting player/dealer hand per game
class gameScore():
    
    def __init__(self, player, dealer, bet):
        self.player = player
        self.dealer = dealer
        self.bet = bet
        
    def reset(self):
        self.player.reset()
        self.dealer.reset()
            
    def calculateScore(self):
        
        if self.player.points == self.dealer.points or (self.player.points > 21 and self.dealer.points > 21):
            print('Player - Dealer Draw')
            
        elif self.player.points <= 21 and (self.player.points > self.dealer.points or self.dealer.points > 21):
            print('Player Wins')
            self.player.winBet(self.bet)
        
        else:
            print('Player Loses')
            self.player.loseBet(self.bet)
        


#validates bet amount input by user  
def playerBet(player):
    
    if player.moneypot <= 0:
        return False
  
    while True:
        
        try:
            valid_input = int((input("How much do you want to bet? ")))
            assert(player.moneypot - valid_input >= 0 and valid_input > 0)
            
        except (AssertionError, ValueError):
            print("Sorry, please enter a valid amount in your moneypot!")

        else:
            
            bet = doubleDownInput(valid_input, player)
            
            print(f"Player is betting: £{bet}")
            
            return bet


#doubles value of bet
def doubleDownInput(valid_input, player):
    
    if (player.moneypot - (valid_input * 2) <= 0):
        return valid_input
    
    while True:
        
        try:
            valid_bet = (input("Do you want to double your bet? y/n ")).lower()
            assert(valid_bet == "y" or valid_bet == "n")
            
        except (AssertionError, ValueError):
            print("Sorry, please enter y (yes) or n (no)")

        else:
            
            if valid_bet == "y":
                valid_input *= 2
            
            return valid_input


#validates player's move input
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
     
     
#deal for both player and dealer
def deal(player, dealer, carddeck, points):
    
    table = [player, dealer]

    for hand in table:
        hand.hit(carddeck.pop())
        hand.calculatePoints(points)
        print(hand)
        hand.showHand()
        print('*'*10)
    
    return player, dealer, carddeck



def dealerOnlyDeal(dealer, carddeck, points):
    
    while dealer.points <= 17:
        dealer.hit(carddeck.pop())
        dealer.calculatePoints(points)
        dealer.showHand()
        print(dealer)
        print('*'*10)
    
    
#validates user input to create new game
def newGameInput(player):
    
    while True:
        try:
            newGameInput = (input("Do you want to play a new game? y/n ")).lower()
            assert(newGameInput == "y" or newGameInput == "n")
    
        except (AssertionError, ValueError):
            print("Sorry, please enter y (yes) or n (no)")
        
        else:
            if newGameInput == "y":
                return True
            
            else:
                return False


#one round of game plus resetting values for dealer/player hands
def playGame(player, dealer, deck, points):
    
    bet = playerBet(player)
    if not bet:
        return 'Game Over'
    
    newgame = gameScore(player, dealer, bet)
        
    while player.points <= 21 and playerMoveInput():
        player, dealer, deck = deal(player, dealer, deck, points)
    
    dealerOnlyDeal(dealer, deck, points)
    
    newgame.calculateScore()
    print(f'Total: £{player.moneypot}')
    newgame.reset()

    
    