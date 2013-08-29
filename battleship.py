"""
Simple Battleship
By Jeff
"""
# Import random integer function.
from random import randint

# Create empty list called board.
board = [] 

# Fill board with 5 lists of 5 "O"s.
for x in range(5):
    board.append(["O"] * 5)

# Function to print board without quotes, in rows.
def print_board(board):
    for row in board:
        print " ".join(row)

# Let's begin with a welcome message:
print "Let's play Battleship!"
# Function to randomize what row the ship is in.
def random_row(board):
    return randint(0, len(board) - 1)

# Function to randomize what column the ship is in.
def random_col(board):
    return randint(0, len(board[0]) - 1)

# Assign random numbers to variables for row/column.
ship_row = random_row(board)
ship_col = random_col(board)

# Print where the ship is, for debugging.
#print "The ship is located at: X:" + str(ship_row) + " Y:" + str(ship_col)


# for loop to limit number of turns player gets.
for turn in range(4):
    # Print board and turn number.
    print "Turn " + str(turn + 1)
    print_board(board)
    
    # Let user guess where the ship is.
    guess_row = int(raw_input("Guess Row:"))
    guess_col = int(raw_input("Guess Col:"))
    
	# Check guess to see if it is a hit or not
	# Hit
    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk my battleship!"
        break
	# Miss
    else:
		# Check to see if guess is not on the board.
        if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
            print "Oops, that's not even in the ocean."
		# Check to see if guess is a repeat.
        elif(board[guess_row][guess_col] == "X"):
            print "You guessed that one already."
		# Guess is valid miss that is not a repeat, mark board with an X.
        else:
            print "You missed my battleship!"
            board[guess_row][guess_col] = "X"
		# End game if turns are all gone.
    if turn == 3:
        print "Game Over!"
        print "My battleship was located at coordinates: X:" + str(ship_row) + " Y:" + str(ship_col)
        break
