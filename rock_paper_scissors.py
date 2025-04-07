import random

userScore = 0
aiScore = 0
options = ['rock', 'paper', 'scissors']
while True:
    userInput = input(
        ('Which is it, Rocks/Paper/Scissors? or Q to quit: ')).lower()
    if userInput == 'q':
        break

    if userInput not in ['rock', 'paper', 'scissors']:
        continue
    randomNumber = random.randint(0, 2)
    # Rock:0, Paper:1, Scissors:2
    aiChoice = options[randomNumber]
    print(f'The computer chose: {aiChoice}.')

    if userInput == 'rock' and aiChoice == 'scissors':
        print('You win')
        userScore += 1
    elif userInput == 'paper' and aiChoice == 'rock':
        print('You win')
        userScore += 1
    elif userInput == 'scissors' and aiChoice == 'paper':
        print('You win')
        userScore += 1
    else:
        print('You lost')
        aiScore += 1

print(f'You won {userScore} games')
print(f'Computer won {aiScore} games')
print("Leave a rating")
