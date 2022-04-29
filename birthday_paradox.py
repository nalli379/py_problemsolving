#Birthday Paradox
#in a set of n randomly chosen people at least 2 will share a birthday
#probability of a shared birthday > 50% in a group of 23 people
#Monte Carlo simulation to estimate the probability for a random event

import calendar
import datetime
import random

month_name = []
for i in range(1, 13):
    month_name.append(calendar.month_name[i])

month_names = dict(enumerate(month_name, start=1))

numDays = []
for i in range(1, 13):
    numDays.append(calendar.monthrange(year=datetime.date.today().year, month=i)[1])

numDays_month = dict(enumerate(numDays, start=1))



def generate_randomBirthday():
    randomMonth = random.randint(1, 12)
    randomDay = random.randint(1, numDays_month.get(randomMonth))
    randomBirthday = (randomDay, randomMonth)
    
    return randomBirthday



def generate_num_randomBirthdays(num):
    
    birthday_count = dict()

    for i in range(num):
        new_birthday = generate_randomBirthday()
        birthday_count[new_birthday] = birthday_count.get(new_birthday, 0) + 1
    
    return check_matches_num_randomBirthdays(birthday_count)



def check_matches_num_randomBirthdays(randombirthdayscount):
    
    count_matches = sum(1 for i in randombirthdayscount.values() if i > 1)
    count_people = sum(i for i in randombirthdayscount.values() if i > 1)

    if count_matches >= 1:
        count_matches = 1
        
    return count_matches, count_people 



def simulate_randomBirthdays(user_num, num_simulations):
    total_matchCount = 0
    total_matchPeople = 0
    
    for i in range(num_simulations):
        simulation_matchCount, simulation_matchPeople = generate_num_randomBirthdays(user_num)
        total_matchCount += simulation_matchCount
        total_matchPeople += simulation_matchPeople
    
    
    probability_match = round((total_matchCount/ (num_simulations)) * 100, 2)
    
    return total_matchCount, total_matchPeople, probability_match


def validate_input():
    while True:
        try:
            valid_num = int(input("How many birthdays do you want to generate for each simulation? Max 100" ))
        except ValueError:
            print("Sorry, I didn't understand the input.")
            continue
        else:
            if 0 < valid_num and valid_num <= 100:
                break
            else:
                print("Sorry, please enter a number between 1-100!")
                continue
    
    return valid_num


def main():
    num_simulations = 10000
    user_input_num = validate_input()
    total_match_count, total_match_people, probability_match_percent  = simulate_randomBirthdays(user_input_num, num_simulations)
    
    statement = f"Total number of people who shared a birthday: {total_match_people}\nThe probability that there will be a matching birthday in a group of {user_input_num} people is {probability_match_percent}%"
    print(statement)
    
main()