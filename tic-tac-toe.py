from itertools import combinations_with_replacement  
  
arr = ["X","O"," "]
r = 3

comb = combinations_with_replacement(arr,r)

lis = []

for i in comb:
    i = ''.join(i)
    lis.append(i)

comb1 = combinations_with_replacement(lis,3)
count = 0
    

#checks the board is valid or not
def validTicTacToe(board):
    count_x, count_o = 0,0 
    # count
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == "X":
                count_x += 1
            elif board[i][j] == "O":
                count_o += 1

  
    if count_o not in {count_x, count_x-1}:
        return False
    
    def isWinner(player):
        for i in range(3):
            if board[i][0] == board[i][1] == board[i][2] == player:
                return True
            
            if board[0][i] == board[1][i] == board[2][i] == player:
                return True
    
        if board[0][0] == board[1][1] == board[2][2]  == player or board[0][2] == board[1][1] == board[2][0] == player:
            return True
        
        return False
    
    if isWinner("X") and count_x != count_o + 1:
        return False
    if isWinner("O") and count_x != count_o:
        return False
    
    return True


for i in comb1:
    if validTicTacToe(list(i)):
        count = count+1
        # uncomment this to print the all possiable boards
        print("\n".join(map(str,list(i))))
        print("--------------------------")
        
#prints count the all possible boards     
print(count)