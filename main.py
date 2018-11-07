import tools as ts
import sw_func as sf

board=ts.board(10,15)

for y in range(15):
    for x in range(10):
        board[y][x]=[" "]

        
ts.arrange(board)
origin = sf.FirstPut(board)

while True: 
    board = sf.put(origin,board)
    ts.arrange(board)
