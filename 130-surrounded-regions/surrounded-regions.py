class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows=len(board)
        cols=len(board[0])
        #step1: check O's in borders and convert to T's
        def convert(r,c):
            if(r<0 or c<0 or r==rows or c==cols or board[r][c]!="O"):
                return
            board[r][c]="T"
            convert(r-1,c)
            convert(r+1,c)
            convert(r,c+1)
            convert(r,c-1)

        for i in range(rows):
            for j in range(cols):
                if (i in [0,rows-1] or j in [0,cols-1]) and (board[i][j]=="O"):
                    convert(i,j)

        #step2: iterate through board and convert O's to X 
        for i in range(rows):
            for j in range(cols):
                if board[i][j]=="O":
                    board[i][j]="X"
                elif board[i][j]=="T":
                    board[i][j]="O"
                

        