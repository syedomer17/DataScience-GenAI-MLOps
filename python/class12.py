import random 

num = random.randint(1,100)

tries = 0


while True: 
    guees = int(input("Guess a number between 1 and 100: "))
    tries += 1 

    if guees == num: 
        print("Congratulations! You guessed the number in", tries, "tries.")
        break
    elif guees < num: 
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")



score = 0 
computer_score = 0

while True: 
    choose = int(input("Enter 1 for stone, 2 for paper, 3 for scissors: "))

    computer = random.randint(1,3)

    if choose > 3 or choose < 1:
        print("Invalid choice! Please choose 1, 2, or 3.")

    if choose ==  1 and computer == 3: 
        print("You win! stone beats scissors.")
        score += 1
    elif choose == 2 and computer == 1: 
        print("You win! paper beats stone.")  
        score += 1
    elif choose == 3 and computer == 2: 
        print("You win! scissors beats paper.")
        score += 1
    elif choose == computer:
        print("It's a tie!")
    else: 
        print("You lose! Computer wins.")
        computer_score += 1

    if score == 5: 
        print("Congratulations! You won the game with a score of", score)
        break
    elif computer_score == 5:
        print("Computer wins the game with a score of", computer_score)
        break