#Birthday Paradox
#in a set of n randomly chosen people at least 2 will share a birthday
#probability of a shared birthday > 50% in a group of 23 people

#generate 23 random birthdays -- see percentage of matching birthdays if generating 23 birthdays 100,000 times
import calendar
import datetime
import random
from collections import Counter


num_simulations = 100000

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
    # print(month_names.get(randomMonth))
    # print(randomDay)
    return randomBirthday



def generate_23_randomBirthdays():
    
    birthday_count = dict()

    for i in range(23):
        new_birthday = generate_randomBirthday()
        birthday_count[new_birthday] = birthday_count.get(new_birthday, 0) + 1
    
    return check_matches_23_randomBirthdays(birthday_count)



def check_matches_23_randomBirthdays(randombirthdayscount):
    count_matches = sum(1 for i in randombirthdayscount.values() if i > 1)
    # print(count_randomBirthdays)
    # list = [i for i, count in randombirthdayscount.items() if count > 1]

    return count_matches   



def simulate_randomBirthdays():
    total_matchCount = 0
    
    for i in range(num_simulations):
        simulation_matchCount = generate_23_randomBirthdays()
        total_matchCount += simulation_matchCount
    
    # print(total_matchCount)
    match_probability = round(total_matchCount / num_simulations, 2)

    return match_probability


def main():
    result =simulate_randomBirthdays()
    # print(result)
    return result

main()