import random


def random_location(size):
    x, y = random.randrange(size), random.randrange(size)
    return x, y


def print_board(board):
    for row in board:
        print(row)


def initialize_board(size):
    # 0 for nothing, 1 for diamond, 2 for start
    board = []
    for i in range(size):
        row = []
        for j in range(size):
            row.append(0)
        board.append(row)

    x, y = random_location(size)
    board[x][y] = 1
    feasible = False
    while not feasible:
        sx, sy = random_location(size)
        feasible = x != sx and y != sy
    board[sx][sy] = 2

    return board, sx, sy


def random_visit(board, sx, sy):
    size = len(board)
    found = False
    steps = 0

    cx, cy = sx, sy
    while not found:
        ocx, ocy = cx, cy
        up = random.randrange(2) == 0
        left = random.randrange(2) == 0
        if up:
            cy += 1
        else:
            cy -= 1
        if left:
            cx += 1
        else:
            cx -= 1
        if cx > size - 1 or cx < 0:
            cx = ocx
        if cy > size - 1 or cy < 0:
            cy = ocy
        steps += 1
        found = board[cx][cy] == 1
    return steps


if __name__ == '__main__':
    size = 4
    seed = None
    visit = random_visit

    if seed is not None:
        random.seed(seed)

    print('Initializing board with size {}.'.format(size))
    board, sx, sy = initialize_board(size)
    print_board(board)
    steps = visit(board, sx, sy)
    print('It took {} step(s) to locate the diamond.'.format(steps))

