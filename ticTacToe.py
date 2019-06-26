theBoard = {
    'top-L': '0', 'top-M': '0', 'top-R': '0',
    'mid-L': '', 'mid-M': 'X', 'mid-R': 'X',
    'low-L': '', 'low-M': '', 'low-R': ''
}


def print_board(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])


print_board(theBoard)