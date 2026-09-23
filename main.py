import random
choices=["Rock","paper","scissors"]
user_score=0
computer_score=0
draws=0
print("ROCK PAPER SCISSORS")
print("ROCK PAPER SCISSORS")
print("ROCK PAPER SCISSORS")
while True:
    print("choose your option:")
    print("1.Rock")
    print("2.Paper")
    print("3.Scissors")
    print("4.Exit")
    choice=input("Enter your choice:")
    if choice=="4":
        break
    if choice=="1":
        user_choice="rock"
    elif choice=="2":
        user_choice="paper"
    elif choice=="3":
        user_choice="scissors"
    else:
        print("Invalid choice! Please enter 1,2,3 or 4.")
        continue
    computer_choice=random.choice(choices)
    print("Your choice:",user_choice)
    print("Computer choice:",computer_choice)
    if user_choice==computer_choice:
        print("Result: Draw!")
        draw+=1
    elif((user_choice=="rock" and computer_choice=="sessors") or
         (user_choice=="paper" and computer_choice=="rock") or
         (user_choice=="scissors" and computer_choice=="paper")):
        print("Result: You win!")
        user_score +=1
    else:
        print("Result: Computer Wins!")
        computer_score +=1
    print("Current Score")
    print("Your Score:",user_score)
    print("Computer Score:",computer_score)
    print("Draws:",draws)
print("FINAL SCORE")
print("FINAL SCORE")
print("FINAL SCORE")
print("Your Score:",user_score)
print("Computer Score:",computer_score)
print("Draws:",draws)
if user_score>computer_score:
    print("Overall Result: You Win!")
elif computer_score>user_score:
    print("Overall Result: Computer Wins!")
else: 
    print("Overall Result: Overall Draw!")
print("Thank you for playing")