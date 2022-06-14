from alt_blackjack_game import *
import random

def main():
    
    #create a player
    player = Player()
    
    #create a dealer
    dealer = Dealer()
    
    #create points dictionary
    points = cardPoints()
    
    while player.moneypot > 0 and newGameInput(player):
        #new deck per game
        deck = cardDeck()
        playGame(player, dealer, deck, points)
    
    print('Thanks for playing')
    
      
main()



  