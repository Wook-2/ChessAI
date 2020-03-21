import chess
import random
import os
import time


BOLD = '\033[1m'
CEND = '\033[0m'
CRED = '\033[31m'
CGRAY = '\033[90m'


class LinkedList:
    class Node:
        def __init__(self, move, init_reward, prev):
            self.move = move
            self.reward = init_reward
            self.prev = prev
            self.next = []

    def __init__(self):
        self.head = self.Node(None, None)
        self.size = 0

    def insert(self, move, init_reward, p):
        n = self.Node(move, init_reward, p)
        p.next.append(n)
        self.size += 1


# board.move_stack을 사용, 마지막 움직임 출력
def last_move():
    move_list=[]
    for i in board.move_stack:
        move_list.append(str(i))
    if len(move_list) > 0 :
        print('\nmove: %s'%(move_list[-1]))


# display
def display():
    reboard = str(board)
    for i in range(len(reboard)):
        if reboard[i].islower() is True:
            print(CRED+BOLD+reboard[i]+CEND, end='')
        elif reboard[i].islower() is False:
            print(reboard[i], end='')
        else:
            print(CGRAY+BOLD+reboard[i]+CEND, end='')
    print()
    last_move()

    # 누적 잡은 말 출력
    for i in range(12):
        if piece[i][1] >= 1:
            print('%s: %d'%(piece[i][0],piece[i][1]))


# 잡은 말 count
def captured_count(before_board, after_board):
    before_list=[0]*12
    after_list=[0]*12

    for i in range(len(before_board)):
        for j in range(len(piece_list)):
            if piece_list[j] is before_board[i]:
                before_list[j] += 1

    for i in range(len(after_board)):
        for j in range(len(piece_list)):
            if piece_list[j] is after_board[i]:
                after_list[j] += 1

    for i in range(len(before_list)):
        if before_list[i] > after_list[i]:
            if (sum(before_list) > sum(after_list)):
                piece[i][1]+=1


board = chess.Board()
piece_list = ['p','r','n','b','q','k','P','R','N','B','Q','K']
piece = []
for i in range(12):
    line = [0, 0]
    piece.append(line)
    piece[i][0]= piece_list[i]

os.system('clear')
display()

# 상수 설정
init_reward = 0.5
epsilon = 0.7 # epsilon의 확률로 랜덤
random_value = random.random()

while True:
    legal_list = []
    for i in board.legal_moves:
        legal_list.append(str(i))

    # epsilon의 확률로 랜덤
    if epsilon <= random_value:
        selected_move = chess.Move.from_uci(random.choice(legal_list))
    else:
        print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        selected_move = chess.Move.from_uci(random.choice(legal_list))

    before_board = str(board)
    board.push(selected_move)
    after_board = str(board)
    captured_count(before_board, after_board)

    os.system('clear')
    display()

    if board.is_game_over() is True:
        print()
        print(board.result())
        if board.result() == "1-0":
            print('\nWHITE win\n')
            break
        elif board.result() == "0-1":
            print('\nBLACK win\n')
            break
        elif board.result() == "1/2-1/2":
            print('\nDraw!\n')
            break