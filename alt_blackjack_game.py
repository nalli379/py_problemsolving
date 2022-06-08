import random

#create a basic player class (parent)
    #stores values of cards in hand
    #stores points per round for game
        #value of ace varies per game

    #can hit to retrieve card
    #show cards 

class tableHand ():
    def __init__(self):
        self.hand = []
        self.points = 0
    
    #take card deck out of function and put in main
    def hit(self, card):
        self.newcard = card
        self.hand.append(self.newcard)
        return self.hand
    
    
    def calculatePoints(self, cardPointsDict):
        
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


#create a dealer class (child)
    #can hit cards when under 17 points
class Dealer(tableHand):
    
    def hit(self, card):
        if self.points >= 17:
            print('Dealer Stays')
            
        else:
            self.newcard = card
            self.hand.append(self.newcard)
        
        return self.hand



#creates a player class (child)
    #creates a money pot for the person
    #bet methods    
class Player(tableHand):
    def __init__(self):
        self.moneypot = 5000
        super().__init__()
    
    #create functions to check a bet amount input (already test double down in main
    #if the bet is possible, return true
    def checkBet(self, bet):
        if self.moneypot - bet < 0:
            return False
        else:
            return True
    
    
    #create a function to add bet amount to money pot with a win
    def winBet(self, bet):
        self.moneypot += bet
        return self.moneypot
    
    #create a function to subtract bet amount to moneypot with a lose
    def loseBet(self, bet):
        self.moneypot -= bet
        return self.moneypot
    



#create a pack of cards class
    #creates a pack of cards
    #deals cards
    #pops a card from the deck
    
class cardsDeck():
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


    ###check the append method!!!!
    def dealCards(self, table):
        self.table = table
      
        for hand in self.table:
            while len(hand) < 2:
                hand.append(self.newDeck.pop())
    
        return self.table
    
    
    def pop(self):
        return self.newDeck.pop()
    
    

#create a points class
    #creates a points dictionary
    #scores points to the first card in a hand
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
        
        
new = cardsDeck()

points = cardPoints()

table = ([('Clubs', 'Ace')], [('Hearts', 2)])

new.dealCards(table)

dealer = Dealer()
player = Player()

player.checkBet(400)





# print('****')
# dealer = Dealer()
# print(dealer.points)
# print(dealer.hand)
# dealer.hit(new.pop())
# print(dealer.calculatePoints(points))
# dealer.hit(new.pop())
# print(dealer.calculatePoints(points))
# dealer.hit(new.pop())

# print(player.moneypot)
# print(player.hand)
# print(player.points)

# player.hit(new.pop())
# print(player.calculatePoints(points))
# player.showHand()

# player.hit(new.pop())
# print(player.calculatePoints(points))

# player.showHand()


# player.hit(new.pop())
# player.addPoints(points)
# player.hit(new.pop())
# player.addPoints(points)




    



















#create a dealer
#create a player

#create a new game object 
#call the create a deck method

#check how much the player wants to bet

#deal cards to dealer, player 
#show cards of dealer player
#show points value for dealer, player

#check if the player wants to hit/stay
#if the player hits
    #deal cards to dealer, player 
#if the player stays
    #check if dealer < 17. if so hit for dealer, else score results
    
