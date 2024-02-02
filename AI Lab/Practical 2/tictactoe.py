## Building a basic Tic Tac Toe Game
import time
import random

# Global Variables
board = [
            "-", "-", "-",
            "-", "-", "-",
            "-", "-", "-"
        ]

current_player = "A"
winner = None 
game_still_going = True
Versus = "human" # or "computer"

# Display the board
def display_board():
    global board
    for i in range(0,9,3): 
        print(board[i] + " | " + board[i+1] + " | " + board[i+2])
        if(i< 6) : 
            print("---------")


def switch_player() : 
    global current_player
    if(current_player == "A") : 
        current_player = "B"
    else : 
        current_player = "A"

def check_winner(): 
    global winner
    check_rows()
    check_columns()
    check_diagonals()
    check_tie()
    if(winner): 
        return winner 
    else: 
        return False

def check_rows() :
    global game_still_going, winner
    if(board[0] == board[1] == board[2] != "-") :
        if(board[0] == "A") : 
            winner = "A"
        else: 
            winner = "B"
        game_still_going = False
    elif(board[3] == board[4] == board[5] != "-") : 
        if(board[3] == "A") : 
            winner = "A"
        else: 
            winner = "B"
        game_still_going = False
    elif(board[6] == board[7] == board[8] != "-") : 
        if(board[6] == "A") : 
            winner = "A"
        else: 
            winner = "B"
        game_still_going = False

def check_columns() :
    global game_still_going, winner
    if(board[0] == board[3] == board[6] != "-") : 
        if(board[0] == "A") : 
            winner = "A"
        else: 
            winner = "B"
        game_still_going = False
    elif(board[1] == board[4] == board[7] != "-") : 
        if(board[1] == "A") : 
            winner = "A"
        else: 
            winner = "B"
        game_still_going = False
    elif(board[2] == board[5] == board[8] != "-") : 
        if(board[2] == "A") : 
            winner = "A"
        else: 
            winner = "B"
        game_still_going = False

def check_diagonals() :
    global game_still_going, winner
    if(board[0] == board[4] == board[8] != "-") : 
        if(board[0] == "A") : 
            winner = "A"
        else: 
            winner = "B"
        game_still_going = False
    elif(board[2] == board[4] == board[6] != "-") : 
        if(board[2] == "A") : 
            winner = "A"
        else: 
            winner = "B"
        game_still_going = False


def check_tie() :
    global game_still_going
    if("-" not in board and (winner != "A" or winner != "B")) : 
        game_still_going = False
        print("It's a tie")

def computer_turn() :
    global board
    position = random.randint(1,9)

    if(board[position-1] == "-") : 
        print(board)
        print("...Computer's Turn...thinking")
        time.sleep(1)
        print("Final: " + str(position), "Index", position-1)
        return position
        
    
    print("Computer's Turn: " + str(position), "Index", position-1)
    return computer_turn()


def player_turn() : 
    global current_player, board, winner, Versus
    position = -1
    if(Versus == "computer" and current_player == "B") : 
        position = computer_turn()
    else : 
        position = int(input("Enter the position to place your mark(1-9): "))
        if(position < 1 or position > 9) : 
            print("Invalid input. Choose a position from 1-9: ")
            return player_turn()
        
        if(board[position-1] != "-") :
            print("You can't go there. Go again.")
            return player_turn()
        
    board[position-1] = current_player
    print("Current Board: ")
    display_board()
    # check for win
    if(check_winner()) : 
        print("Winner: " + winner)
    
    # switch player
    switch_player()





# Start the game
def start_game() : 
    global winner, game_still_going, current_player, Versus
    print("Welcome to Tic Tac Toe")
    display_board()

    print("Choose your opponent: ")
    print("1. Human")
    print("2. Computer")

    ch = int(input("Enter your choice: "))
    if(ch == 1) : 
        Versus = "human"
    else : 
        Versus = "computer"


    while game_still_going : 
        player_turn()
        if(winner == "A" or winner == "B") : 
            print(winner + " won")
            break



    play_again = input("Do you want to play again? (yes/no): ")
    if(play_again == "yes") : 
        for i in range(0,9) : 
            board[i] = "-"
            game_still_going = True
            winner = None
            current_player = "A"
        start_game()
    else : 
        print("Thanks for playing")

start_game()