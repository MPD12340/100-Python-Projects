import random

num = random.randint(1, 10)
count = 0
while True:
    guess = int(input('enter the number to check if it matches : '))
    count = count + 1
    if guess > num:
        print('Guess is slightly higher ! try to come bit lower')
    elif guess < num:
        print('Guess is slightly lower ! try to come bit higher')
    else:
        if guess == num:
            print('yay ! ')
            break
        else:
            print('Try again.')

print(
    f"It took you nearly {count} times to guess the number and the number is {num}")
