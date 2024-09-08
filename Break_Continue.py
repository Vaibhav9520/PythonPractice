# Break Keyword
'''
for i in range(1,21):
    if i == 10:
        break
    print(i)
print("New line")

# continue Keywork
for i in range(1,21):
    if i == 10:
        continue
    print(i)
    '''
# Making a number gussing game!!!!!!
'''

import random
winning_number = random.randint(1,100)
guess = 1
number = int(input("Guess a number between 1 to 100: "))
game_over = False

while not game_over:
    if number == winning_number:
        print(f"You win,and you gussesed this number in {guess} times")
        game_over = True
    else:  #[DRY principle : Don't repeat yourself]
        if number < winning_number:
            print("Too low")
        else:
            print("Too heigh")

        guess +=1
        number = int(input("Guess again : "))
        '''
#Step Argument!!!!!!!!
'''
for i in range(0,20,2):#here third argument is step argument
    print(i)'''
# Print negative number
for i in range(10,1,-1):
    print(i)