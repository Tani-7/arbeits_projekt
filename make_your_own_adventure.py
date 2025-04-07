name = input("Enter your name")
print(f'Welcome {name} to this Rally Adventure')

choice = input("You are on a rally stage abd there is a big boulder in the middle of the road, you can only go left or right. Where are you stering left, or right")

if choice == 'left':
    choice == input('There are rowdy fans on the side of the road, you can handbrake around them or go through with hopes they get out of the way. Type handbrake to use handbrake or push to go ahead.').lower()
    if choice == 'handbrake':
        print('You turned sharply and lost too much speed')
    elif choice == 'push':
        print('You pushed through but the fans did not move ut the way, are you trying to get us cancelled!!!')
    else:
        print('Not a valid option, YOU LOSE!')
elif choice == 'right':
    choice = input('There is a big mud puddle that wasn\'t there during the recce. You can handbrake and go around or push through and make a spectacle for the fans ').lower()
    if choice == 'handbrake':
        print('You lost too much speed, your competitor is catching up')
    elif choice == 'push':
        print('You made a big splash and earned more driver of the weekend points')
    else:
        print('Not a valid option, YOU LOSE!!!')
else:

    print('This is not a valid option')


print(f'Thank you for playing, {name}')
