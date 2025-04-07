import random

max_range = input("Type a number: ")

if max_range.isdigit():
    max_range = int(max_range)

    if max_range == 0:
        print(f"{max_range} is too low, enter a higher number")
        quit()
else:
    print("Please insert a number")
    quit()

random_number = random.randint(0, max_range)
guesses = 0
while True:
    guesses += 1
    guess = input('Make a guess: ')
    if guess.isdigit():
        guess = int(guess)
    else:
        print('Please enter a digit')
        continue

    if guess == random_number:
        print(f'Yaay!! you got it {guess} is the correct number')
        break
    elif guess > random_number:
        print('Too high')
    else:
        print('Too low')

print(f'you got it in {guesses} guesses')
