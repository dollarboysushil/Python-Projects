import random

print("Guess Number Between [0 -100)")
number  = random.randrange(100)

Lives = 7

flag = False
while flag == False:
    guess = (input("Guess: "))
    
    if guess != "quit":
        guess = int(guess)
        if Lives != 0:
            if guess > number:
                print("Try guessing smaller number:")
                Lives = Lives -1
                
            elif guess < number:
                print("Try guessing higher number")
                Lives = Lives -1
                
            elif guess == number:
                print("You have successfully gussed the number.")
                print(f"Life used  {7 - Lives}")
                flag = True
                
                
        else:
            print("Out of lives. You Lose!!")
            flag = True
        
    elif guess == "quit":
        print("you quitted the game!")
        flag= True

