import random

highest = 10
answer = random.randint(1, highest)
print(answer) #TODO: Remove after testing
guess = 0 # initialise to any number that doesnt equal the answer
print("Please guess a number between 1 and {}: ".format(highest))

while guess != answer:
    guess = int(input())

    if guess == 0:
        break
    if guess == answer:
        print("well done, you guessed it")
    else:
        if guess < answer:
            print("Please guess higher")
            break
        else:
            print("Please guess lower")
        # guess = int(input())
        # if guess == answer:
        #     print("well done you guessed it")
        # else:
        #     print("Sorrry you have not guessed correctly")






# if guess  < answer:
#     print("Please guess higher")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it")
#     else:
#         print("Sorry you have not guessed correctly")
# elif guess > answer:
#     print("Please guess lower")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it")
#     else:
#         print("Sorry you have not guessed correctly")
# else:
#     print("You got it first time!!!! :)")