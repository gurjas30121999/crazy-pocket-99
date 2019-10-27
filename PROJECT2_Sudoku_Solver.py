#SETTING UP THE SUDOKU BOARD:
board=[
    [0,0,0,0,5,0,0,0,0],
    [0,0,0,7,0,0,1,0,2],
    [0,4,0,0,9,0,0,0,8],
    [0,6,0,4,3,0,8,9,0],
    [7,0,0,0,0,0,0,0,0],
    [0,0,0,8,0,0,0,0,6],
    [2,0,4,0,0,0,0,0,0],
    [1,5,0,0,0,0,0,0,0],
    [0,3,0,0,0,9,0,5,4]
    ]
def printboard(bo):
    for i in range(len(bo)):
        if i%3==0 and i!=0:
            print("- - - - - - - - - - - - - - - - -")
        for j in range(len(bo[0])):
            if j%3==0 and j!=0:
                print("|",end=" ")
            if j==8:
                print(bo[i][j])
            else:
                print(str(bo[i][j])+" ",end=" ")


#CHECKING EMPTY SQUARES:
def isempty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j]==0:
                return (i,j)

    return None

#CHECKING VALIDITY:
def isvalid(bo, num, pos):
    #CHECKING ROWS:
    for i in range(len(bo[0])):
        if bo[pos[0]][i]==num and pos[1]!=i:
            return False
    #CHECKING COLUMNS:
    for i in range(len(bo)):
        if bo[i][pos[1]]==num and pos[0]!=i:
            return False
    #HCEKCING BOX:
    boxx=pos[1]//3
    boxy=pos[0]//3
    for i in range(boxy*3,boxy*3+3):
        for j in range(boxx*3,boxx*3+3):
            if bo[i][j]==num and (i,j)!=pos:
                return False
    return True
#SOLVING:
def solve(bo):
    find =isempty(bo)
    if not find:
        return True
    else:
        row, col=find
    for i in range(1,10):
        if isvalid(bo,i,(row,col)):
            bo[row][col]=i
            if solve(bo):
                return True
            bo[row][col]=0
    return False

printboard(board)
solve(board)
print("________________________________________________________________")
print("________________________________________________________________")
printboard(board)

    
