k = 1

def Safe(board, row, col) : 
	
	n=len(board)

	for i in range(col): 
		if (board[row][i]): 
			return False
	i = row 
	j = col 
	while i >= 0 and j >= 0: 
		if(board[i][j]): 
			return False; 
		i -= 1
		j -= 1

	i = row 
	j = col 
	while j >= 0 and i < n: 
		if(board[i][j]): 
			return False
		i = i + 1
		j = j - 1

	return True

def FindSol(board, col) : 

	n=len(board)

	if (col == n): 
		print_board(board) 
		return True

	Result = False
	for i in range(n): 
	
		if (Safe(board, i, col)): 
		
			board[i][col] = 1; 
			
			Result = FindSol(board, col + 1); 

			board[i][col] = 0 
	
	return Result 

def print_board(board):

	n=len(board) 

	global k 
	print(k, "-\n") 
	k = k + 1
	for i in range(n): 
		for j in range(n): 
			print(board[i][j], end = " ") 
		print("\n") 
	print("\n")

def PrintAllSolution(n) : 

	board = [[0 for j in range(n)] 
				for i in range(n)] 

	if (FindSol(board, 0) == False): 
	
		return
	return

def main():
	
	PrintAllSolution(8) 

main()

