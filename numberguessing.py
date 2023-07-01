
import random

chances = 8

# Define the range of your numbers!
upperBound = 100

# Return a random number between 0 and upperBound
answer = random.randrange(0, upperBound)

print("Make a guess about the number!")

print("The number is an integer between 0 and " + str(upperBound))

# TODO: Initialize response with the user's input
response = input()

# TODO: Let guess store the integer value of response
guess = int(response)
if (guess == answer):
    print("yay you guessed the number")
# # Repeat until the guess is equal to the answer
while guess != answer:
    if (guess == answer):
        print("yay you guessed the number")
        break
    elif (guess < answer ):
        print("guess a bigger number. You have "+str(chances)+" chances left")
        guess = int(input())
    elif (guess > answer ):
        print("guess a smaller number. You have "+str(chances)+" chances left")
        guess = int(input())
    chances -= 1
    #     # If we don't have any guesses left
    #     # Tell the user they're out of chances, and show the answer
    if (chances == 0):
        # TODO: Enter this if-statement if we run out of chances
        #put following two print statements(39,40) in if condition
        print("You ran out of chances")
        print("The correct number is: " + str(answer))
        break
if (guess == answer):
    print("yay you guessed the number")
# TODO: After printing the above statements, break out of the loop

