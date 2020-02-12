from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
board = [['_','X', 'O'], ['X', '_', 'O'], ['0', 'X', '_']]
def index(request):
	return render(request, "tictactoe/index.html", {"board":board})
	
