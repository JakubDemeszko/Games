import random
paper = 1
rock = 2
scissors = 3
print("Welcome in the Paper, Rock and Scissors game!")
player1 = int(input("Player 1, Choose: Paper is 1, Rock 2, Scissors 3: "))
while player1 != 1 and player1 != 2 and player1 != 3:
    print("You put wrong number, try again!")
    player1 = int(input("Player 1, Choose: Paper is 1, Rock 2, Scissors 3: "))
player2 = int(input("Player 2, Choose: Paper is 1, Rock 2, Scissors 3: "))
while player2 != 1 and player2 != 2 and player2 != 3:
    print("You put wrong number, try again!")
    player2 = int(input("Player 2, Choose: Paper is 1, Rock 2, Scissors 3: "))
if player1 == 1 and player2 == 1:
    print("There is a draw!")
elif player1 == 1 and player2 == 2:
    print("Player 1 won! Congrats! :)")
elif player1 == 1 and player2 == 3:
    print("Player 2 won! Congrats! :)")
elif player1 == 2 and player2 == 1:
    print("Player 2 won! Congrats! :)")
elif player1 == 2 and player2 == 2:
    print("There is a draw!")
elif player1 == 2 and player2 == 3:
    print("Player 1 won! Congrats! :)")
elif player1 == 3 and player2 == 1:
    print("Player 1 won! Congrats! :)")
elif player1 == 3 and player2 == 2:
    print("Player 2 won! Congrats! :)")
elif player1 == 3 and player2 == 3:
    print("There is a draw!")

print("Now its time to play the raffle game! :)") #only from 1 up to 100
number = int(input("Choose the number from 1 to 100: "))
while number < 1 or number > 100:
    print("You put number out of range! Try again!")
    number = int(input("Choose the number from 1 to 100: "))
win = random.randint(1, 100)
### print(win) just to check if the program is working well :)
while win != number:
    print("Unfortunately, you did not win!")
    game = int(input("Do you want to try again? Press 1 if yes, 2 if not: "))
    if game == 1:
        number = int(input("Choose the number from 1 to 100: "))
    elif game == 2:
        print("Thank you for playing the raffle game! Enjoy your day :)!")
        break
if win == number:
    print("Congrats! You won! :)")
