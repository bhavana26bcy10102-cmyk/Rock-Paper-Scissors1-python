import random

ROCK="rock"
PAPER="paper"
SCISSORS="scissors"

MOVES=[ROCK, PAPER, SCISSORS]

RULES={
    ROCK:SCISSORS,
    PAPER:ROCK,
    SCISSORS:PAPER
}

def show_title():
    print("="*50)
    print("ROCK PAPER SCISSORS GAME")
    print("=" * 50)

def show_menu():
    print("1.Start Game")
    print("2.Instructions")
    print("3.Exit")

def show_moves():
    print("n Choose your move:")
    print("1.Rock")
    print("2.Paper")
    print("3.Scissors")

def get_player_move():
    while True:
        show_moves()
        choice=input("Enter your choice:").strip()
        if choice=="1":
            return ROCK
        if choice=="2":
            return PAPER
        if choice=="3":
            return SCISSORS
        print("Invalid choice, Please try again.")

def get_computer_move():
    return random.choice(MOVES)

def find_winner(player, computer):
    if player==computer:
        return "draw"
    if RULES[player]==computer:
        return "player"
    return "computer"

def display_moves(player, computer):
    print("Your move:", player.title())
    print("Computer move:", computer.title())

def display_result(result):
    print()

    if result=="player":
        print("You won this round:")
   
    elif result=="computer":
        print("Computer won this round:")

    else:
        print("This round is a draw:")

def show_instructions():
    print("n" + "=" * 50)
    print("INSTRUCTIONS")
    print("=" * 50)

    print("Rock beats Scissors.")
    print("Paper beats Rock.")
    print("Scissors beats Ppaer.")
    print("If both players choose the same move.")
    print("the round is draw.")

    print("The first player to reach the target score")
    print("Wins the match.")

    print("=" * 50)

def choose_round():
    while True:
        print("Choose match length:")
        print("1.Best of 1")
        print("2.Best of 3")
        print("3.Best of 5")
        print("4.Best of 7")

        choice= input("Enter choice:").strip()

        if choice=="1":
           return 1

        if choice=="2":
           return 3

        if choice=="3":
           return 5

        if choice=="4":
           return 7

        print("Invalid choice.")

def reqquired_score(rounds):
     return rounds // 2 + 1

def display_score(
        player_score,
        computer_score
):
    print("n" + "=" * 50)
    print("SCORE")
    print("-" * 50)
    print("You:", player_score)
    print("Computer:", computer_score)
    print("-" * 50)

def play_round():
    player= get_player_move()
    computer= get_computer_move()

    display_moves(
        player,
        computer
    )
    result= find_winner(
        player,
        computer
    )

    display_result(result)
    return result

def choose_round():
    rounds= input("Enter the number of rounds to play:")
    return int(rounds)

def required_score(rounds):
    return(rounds // 2) + 1

def play_game():
    print("=" * 50)
    rounds= choose_round()
    target= required_score(rounds)

    player_score=0
    computer_score=0
    draw_count=0
    round_number=0

    while(
        player_score < target
        and computer_score < target
    ):
        round_number += 1

        print(
            "n===ROUND{round_number}==="
        )
        result = play_round()

        if result== "player":
            player_score += 1

        elif result== "computer":
            computer_score += 1

        else:
            draw_count += 1

        display_score(
            player_score,
            computer_score
        )

        if(
            player_score < target
            and computer_score < target
        ):
            input(
                "n Press Enter for next round..."
            )

def show_final_result(
        player_score,
        computer_score,
        draw_count
    ):

    print("n" + "=" * 50)
    print("Final Result")
    print("=" * 50)

    print("Your Score:",     player_score)
    print("Computer Score:", computer_score)
    print("Draws:",          draw_count)

    if player_score > computer_score:
        print("Congratulations! You won the match!")

    elif computer_score > player_score:
        print("Computer won the match.")

    else:
        print(" The match ended  in a draw.")
    print("=" * 50)

def ask_replay():
    while True:
        answer= input(" Do u want to play again? (yes/no):").strip().lower()
    if answer== "yes":
        return True
    elif answer== "no":
        return False
    print("Please enter yes or no.")

def start_game():
    while True:
        play_game()

        if not ask_replay():
            break

    print("Thanks for playing!")

def welcome_message():
    print("Welcome to Rock Paper Scissors!")
    print("Have fun and chooseyour move wisely.")

def main():
    show_title()
    welcome_message()

    while True:
        show_menu()

        choice=input(
            "Enter your choice:"
        ).strip()

        if choice== "1":
            start_game()

        elif choice=="2":
            show_instructions()

        elif choice== "3":
            print(
                "Thank you for playing"
                "Rock Ppaer Scissors!"
            )
            break

        else:
             print( 
                 "Invalid menu choice."
            )
if __name__== "__main__":
    main()






     
