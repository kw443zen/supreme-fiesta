import random

play = True
while play:
    print("""
          The Bagels Game
          """)
    nums = str(random.randint(000, 999))
    secretNum = ''

    for i in range(3):
        secretNum += str(nums[i])

    count = 0
    while count < 10:
        guess = ''
        
        while True:
            print("Enter a 3 digit number or type help for help menu\n")
            guess = input("# ")
            
            if guess.lower().startswith("\h"):
                print("""
                    Help Menu:
                    
                    Clues: Fermi = Correct number and position
                           Pico = Correct number, wrong position
                           Bagels = All numbers are wrong
                    """)
            elif len(guess) != 3 or not guess.isdecimal():
                print("Please enter a 3 digit guess")
            else:
                break
            
        if guess == secretNum:
            print("Congratulations! You've guessed it!!!")
            break
          
        count += 1
        clue = []
        for i in range(3):
            if guess[i] == secretNum[i]:
                clue.append("Fermi")
            elif guess[i] in secretNum:
                clue.append("Pico")
                
        if len(clue) == 0:
            print("Bagels")
        else:
            random.shuffle(clue)
            print(' '.join(clue))
        print("You have", 10 - count, "guesses left.")
        
    if count == 10:
        print("The secret number was:", secretNum)
    
    playAgain = input("Would you like to play again? (yes/no)\n")
    if playAgain.lower().startswith("n"):
        play = False