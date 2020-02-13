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
	if "board" not in request.session.keys():
		request.session["board"] = emptyBoard()

	board = request.session["board"]
	print(board)

	if request.method == "POST":
		if board[int(request.POST["row"])][int(request.POST["col"])] == "_":
			board[int(request.POST["row"])][int(request.POST["col"])] = "X"

		if shouldReset(board):
			request.session.flush()
			board = emptyBoard()

		request.session["board"] = board
		
	request.session.modified = True
	return render(request, "tictactoe/index.html", {"board":request.session["board"]} )


	
