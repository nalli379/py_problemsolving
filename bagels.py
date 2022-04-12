import random
import re

#Bagels is a deductive logic game
#guess a three digit number
def guess_number():
    
    #validate input is a three digit number 
    while True:
        try:
            input_guess_num = int(input("Enter a three digit number: "))
        
        #if the input is not valid, repeat request for input   
        except ValueError:
            print("Sorry, I didn't understand that input.")
            continue
        
        else:
            if 100 <= input_guess_num and input_guess_num <= 999:
                break
            
            #if the input is not a three digit number, repeat request for input
            else:
                print("Sorry, please enter a three digit number between 100 - 999! ")
                continue

    return input_guess_num



def check_match(random_num, guess_num):    
    #if the guess matches random three digit number, end game
    if random_num == guess_num:
        print("Match")
        return True
    
    #if the guess doesn't match the three digit number check if any of the digits are in the three digit number
    else:
        guess_num = str(guess_num)
        random_num = str(random_num)
        
        test_fermi = re.findall(f"[{guess_num}]", random_num)
        
        if test_fermi:
            test_pico = re.findall(f"^{guess_num[0]}", random_num) or re.findall(f"\B{guess_num[1]}\B", random_num) or re.findall(f"{guess_num[2]}$", random_num)
            
            #"Pico" if you have correct digit in correct place
            if test_pico:
                print("Pico")
                return False
            
            #Fermi if you have correct digit in wrong place
            else:
                print("Fermi")
                return False
        
        #"Bagels" if you have no correct digits   
        else:
            print("Bagel")
            return False
            

def guess_game():

    count = 0
    
    #generate a new random three digit number
    random_num = random.randint(100, 999)

    #You have 10 chances to guess the random three digit number 
    while count <= 10:
        #get a guess input, increase counter by one
        new_guess = guess_number()
        
        #check if guess matches random three digit number
        guess_match = check_match(random_num, new_guess)
        
        count += 1
        
        if guess_match:
            break

    return "End Game"
        
        
guess_game()