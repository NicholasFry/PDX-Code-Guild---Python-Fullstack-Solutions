#first computer picks 6 random numbers as winner
#second try picking 6 100,000 times
import random
#iterate random numbers into winning list
win_list = random.sample(range(1, 99), 6)
print(win_list)
#this is how much you win if you match numbers:cash
match_cash_dict = {1:4, 2:7, 3:100, 4: 50000, 5:1000000, 6:25000000}
#start your balance at zero

#iterate random numbers for the tickets bought list
for i in range(1, 100000):
    balance -= 2
    matches = 0
    ticket = random.sample(range(1,99), 6)
    if ticket[i] == win_list[i]:
        matches += 1
    else:
        #says return is outside function. No idea.
        return matches

#Looking for matching numbers
'''def num_matches(win_list, tickets):
    matches = 0
    if win_list[i] = tickets[i]
'''

#not sure why this variable is not printing
print(matches)
