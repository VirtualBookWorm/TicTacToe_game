theBoard = {'top-L':' ','top-M':' ','top-R':' ','mid-L':' ','mid-M':' ','mid-R':' ','low-L':' ','low-M':' ','low-R':' ',}
flag = 0
def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])
turn = 'X'
for i in range(9):
    printBoard(theBoard)
    print('turn for ' + turn + '. Move on which space?')
    move = input()
    while(theBoard[move]!=' '):
        print('Space is occupied!!!')
        print('turn for ' + turn + '. Move on which space?')
        move = input()
    theBoard[move] = turn
    if i>=4:
        if(theBoard['top-L']==turn and theBoard['top-M']==turn and theBoard['top-R']==turn):
            print('Winner is ',turn)
            break
        elif(theBoard['mid-L']==turn and theBoard['mid-M']==turn and theBoard['mid-R']==turn):
            print('Winner is ',turn)
            break
        elif(theBoard['low-L']==turn and theBoard['low-M']==turn and theBoard['low-R']==turn):
            print('Winner is ',turn)
            break
        elif(theBoard['top-L']==turn and theBoard['mid-L']==turn and theBoard['low-L']==turn):
            print('Winner is ',turn)
            break
        elif(theBoard['top-M']==turn and theBoard['mid-M']==turn and theBoard['low-M']==turn):
            print('Winner is ',turn)
            break
        elif(theBoard['top-R']==turn and theBoard['mid-R']==turn and theBoard['low-R']==turn):
            print('Winner is ',turn)
            break
        elif(theBoard['top-L']==turn and theBoard['mid-M']==turn and theBoard['low-R']==turn):
            print('Winner is ',turn)
            break
        elif(theBoard['top-R']==turn and theBoard['mid-M']==turn and theBoard['low-L']==turn):
            print('Winner is ',turn)
            break
        else:
            flag = 1
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
printBoard(theBoard)
if flag == 1:
    print('Draw match!!')