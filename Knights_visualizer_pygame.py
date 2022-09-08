import pygame
import time
pygame.init()
screen_dimensions = screen_width, screen_height = 750,750
screen = pygame.display.set_mode((screen_dimensions))
font1 = pygame.font.SysFont("comicsans", 40)
font2 = pygame.font.SysFont("comicsans", 20)
font3 = pygame.font.SysFont("comicsans", 70)
num = 8
x = 0
y = 0
array = [[0 for i in range(num)]for j in range(num)]
dif = screen_width/8
def print_board(board):
    for i in range(len(board[0])):
        print(str(board[i]) + ", ")

chess_board = [
    [1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
]

def get_pos(pos):
    global x
    x = pos[0] // calculate_dif(chess_board)
    global y
    y = pos[1] // calculate_dif(chess_board)

def calculate_dif(board):
    dif = screen_width / len(board[0])
    return dif

def draw_boxes(board):
    for i in range(len(board[0])):
        for j in range(len(board[0])):
            if board[i][j] != 0:
                pygame.draw.rect(screen, (0, 153, 153), (i * calculate_dif(chess_board), j * calculate_dif(chess_board), calculate_dif(chess_board) + 1, calculate_dif(chess_board) + 1))
                text1 = font1.render(str(chess_board[i][j]), 50, (0, 0, 0))
                screen.blit(text1, (i * calculate_dif(chess_board) + 25, j * calculate_dif(chess_board)))
    for i in range(len(board[0])):
        pygame.draw.line(screen, (0,0,0), (i * calculate_dif(board), 0),(i * calculate_dif(board), screen_height),1 )
        pygame.draw.line(screen, (0, 0, 0), (0, i * calculate_dif(board)), (screen_width, i * calculate_dif(board)), 1)

def highlight_box(board, x, y):
    for i in range(2):
        pygame.draw.line(screen, (255, 0, 0), (x * calculate_dif(board) , (y + i) * calculate_dif(board)),
                        (x * calculate_dif(board) + calculate_dif(board) , (y + i) * calculate_dif(board)), 7)
        pygame.draw.line(screen, (255, 0, 0), ((x + i) * calculate_dif(board), y * calculate_dif(board)),
                         ((x + i) * calculate_dif(board), y * calculate_dif(board) + calculate_dif(board)), 7)
n = 8
def isSafe(x, y, board):
    '''
        A utility function to check if i,j are valid indexes
        for N*N chessboard
    '''
    if(x >= 0 and y >= 0 and x < n and y < n and board[x][y] == 0):
        return True
    return False


move_x = [2, 1, -1, -2, -2, -1, 1, 2]
move_y = [1, 2, 2, 1, -1, -2, -2, -1]
def solveKTUtil(n, board, curr_x, curr_y, move_x, move_y, pos):
    '''
        A recursive utility function to solve Knight Tour
        problem
    '''

    if(pos == 64):
        return True

    # Try all next moves from the current coordinate x, y
    for i in range(8):
        new_x = curr_x + move_x[i]
        new_y = curr_y + move_y[i]
        pygame.event.pump()
        if (isSafe(new_x, new_y, board)):
            board[new_x][new_y] = pos
            draw_boxes(chess_board)
            highlight_box(chess_board, new_x, new_y)
            pygame.display.update()


            if (solveKTUtil(n, board, new_x, new_y, move_x, move_y, pos + 1)):
                return True

            # Backtracking
            board[new_x][new_y] = 0
            screen.fill((255,255,255))
            draw_boxes(chess_board)
            highlight_box(chess_board, new_x, new_y)


    return False

def result():
    pygame.draw.rect(screen, (255,255,255), (0, 350, screen_width, 80 ) )
    text1 = font3.render("FINISHED PRESS R", True, (0, 0, 0))
    screen.blit(text1, (0,330))

er = 0
rs = 0
flag1 = 0
highlight = True
run = True
running = False
while run:

    screen.fill((255,255,255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            get_pos(pos)
            highlight = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
            if event.key == pygame.K_RETURN:
                flag1 = 1
            if event.key == pygame.K_r:
                for i in range(8):
                    for j in range(8):
                        chess_board[i][j] = 0
                chess_board[0][0] = 1
                rs = 0

    if flag1 == 1:
        if solveKTUtil(n, chess_board, 0, 0, move_x, move_y, 2):
            rs = 1
            flag1 = 0
        else:
            er = 1
    draw_boxes(chess_board)
    highlight_box(chess_board, x, y)
    if rs == 1:
        result()
    pygame.display.update()
pygame.quit()