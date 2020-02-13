from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def shouldReset(board):
		for row in board:
			if row[0] != '_'  and row[0] == row[1] and row[1] == row[2]:
				return True

		for col in range(0, 3):
			if board[0][col] != '_' and board[0][col] == board[1][col] and board[1][col] == board[2][col]:
				return True
		
		if board[1][1] != '_':
			if board[0][0] == board[1][1] and board[1][1]  == board[2][2]:
				return True

			if board[0][2] == board[1][1] and board[1][1]  == board[2][0]:
				return True
		return False

def emptyBoard():
	return [['_','_', '_'], ['_', '_', '_'], ['_', '_', '_']]

def index(request):
	# If they don't have a board, give them a board
	if "board" not in request.session.keys():
		request.session["board"] = emptyBoard()
	board = request.session["board"]

	# If they are here because they played a move
	if request.method == "POST":
		# Let them play their move
		if board[int(request.POST["row"])][int(request.POST["col"])] == "_":
			board[int(request.POST["row"])][int(request.POST["col"])] = "X"

		# If they won, or we won, then reset the board
		if shouldReset(board):
			board = emptyBoard()

		# Otherwise, we play in any tile that we can, if we can play at all
		else:
			played = False
			for row in range(0,3):
				for col in range(0,3):
					if board[row][col] == "_" and not played:
						board[row][col] = "O"
						played = True
					
		# Send the board back to be rendered
		request.session["board"] = board
		request.session.modified = True

	return render(request, "tictactoe/index.html", {"board":request.session["board"]})


	
