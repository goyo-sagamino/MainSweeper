import random as ran
import tools as ts

#---------------------------------------------------------モジュールrandom,toolsを、ran, ts としてimport------------------------------------------------------

def FirstPut (board):
    boa = board
    for count in range (27):
        X = ran.randint(0,9)
        Y = ran.randint(0,14)

        boa[Y][X] = ['b']
    #ts.arrange(board)
    return boa

#---------------------------------------------------------地雷の設置-------------------------------------------------------------------------------------------
    
def put (origin,board):
    ori = origin
    boa = board

    text = input('x,y')
    x = int(text[0])
    texty = text[2]
    if texty =='A':
        y = 10
    elif texty =='B':
        y = 11
    elif texty =='C':
        y = 12
    elif texty =='D':
        y = 13
    elif texty =='E':
        y = 14
    else:
        y = int(text[2])
        
    num = 0

    if ori[y][x] == ['b']:
        print('='*200,'\n'*4,'Your lose!!','\n'*4,'='*200)

    else:
                
        if x == 0 and y == 0: #or x == 9 and y == 0 or x == 9 and x == 14 or x == 0 and y == 14:
            if ori[y][x+1] == ['b']:
                num += 1
            if ori[y+1][x] == ['b']:
                num += 1
            if ori[y+1][x+1] == ['b']:
                num += 1
            boa[y][x]=[str(num)]

        elif x == 9 and y == 14: #or x == 9 and y == 0 or x == 9 and x == 14 or x == 0 and y == 14:
            if ori[y][x-1] == ['b']:
                num += 1
            if ori[y-1][x] == ['b']:
                num += 1
            if ori[y-1][x-1] == ['b']:
                num += 1
            boa[y][x]=[str(num)]

        elif x == 0 and y == 14: #or x == 9 and y == 0 or x == 9 and x == 14 or x == 0 and y == 14:
            if ori[y][x+1] == ['b']:
                num += 1
            if ori[y-1][x] == ['b']:
                num += 1
            if ori [y-1][x+1] == ['b']:
                num += 1
            boa[y][x]=[str(num)]

        elif x == 9 and y == 0: #or x == 9 and y == 0 or x == 9 and x == 14 or x == 0 and y == 14:
            if ori[y][x-1] == ['b']:
                num += 1
            if ori[y+1][x] == ['b']:
                num += 1
            if ori[y+1][x-1] == ['b']:
                num += 1
            boa[y][x]=[str(num)]

        elif x == 0:
            if ori[y-1][x] == ['b']:
                num += 1
            if ori[y-1][x+1] == ['b']:
                num += 1
            if ori[y][x+1] == ['b']:
                num += 1
            if ori[y+1][x+1] == ['b']:
                num += 1
            if ori[y+1][x] == ['b']:
                num += 1
            boa[y][x]=[str(num)]

        elif x == 9:
            if ori[y-1][x] == ['b']:
                num += 1
            if ori[y-1][x-1] == ['b']:
                num += 1
            if ori[y][x-1] == ['b']:
                num += 1
            if ori[y+1][x-1] == ['b']:
                num += 1
            if ori[y+1][x] == ['b']:
                num += 1
            boa[y][x]=[str(num)]

        elif y == 0:
            if ori[y][x+1] == ['b']:
                num += 1
            if ori[y+1][x+1] == ['b']:
                num += 1
            if ori[y+1][x] == ['b']:
                num += 1
            if ori[y+1][x-1] == ['b']:
                num += 1
            if ori[y][x-1] == ['b']:
                num += 1
            boa[y][x]=[str(num)]

        elif y == 14:
            if ori[y][x-1] == ['b']:
                num += 1
            if ori[y-1][x-1] == ['b']:
                num += 1
            if ori [y-1][x] == ['b']:
                num += 1
            if ori [y-1][x+1] == ['b']:
                num += 1
            if ori [y][x+1] == ['b']:
                num += 1
            boa[y][x]=[str(num)]

        else:
            if ori[y-1][x] == ['b']:
                num += 1
            if ori[y-1][x+1] == ['b']:
                num += 1
            if ori [y][x+1] == ['b']:
                num += 1
            if ori [y+1][x+1] == ['b']:
                num += 1
            if ori [y+1][x] == ['b']:
                num += 1
            if ori [y+1][x-1] == ['b']:
                num += 1
            if ori [y][x-1] == ['b']:
                num += 1
            if ori [y-1][x-1] == ['b']:
                num += 1
            boa[y][x]=[str(num)]


        return boa

#-----------------------------------------------------基本動作------------------------------------------------------------------------------------------------------
