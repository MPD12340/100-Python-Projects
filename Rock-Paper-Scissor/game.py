from ast import main
import random

options = ['rock', 'paper', 'scissor']

count = 0  # game should be atleast played for 5 times
my_wins = 0
bot_wins = 0
while True:

    if count > 5:
        break
    bot_choice = random.choice(options)
    my_choice = input('Enter your choice : ')
    count = count + 1
    if bot_choice == my_choice:
        print('It\'s equal')
    elif (bot_choice == 'rock' and my_choice == 'scissor') or (bot_choice == 'scissor' and my_choice == 'paper') or (bot_choice == 'paper' and my_choice == 'rock'):
        print('bot wins !')
        bot_wins += 1
    elif my_choice in options:
        my_wins += 1
        print('I win ! Hurray')
    else:
        print('Invalid one ! try again')
print(
    f"Okay I won {my_wins} times and bot won {bot_wins} times. So guess who is the winner")

       