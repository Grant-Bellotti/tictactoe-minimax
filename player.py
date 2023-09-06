from random import randint

class Player:
    def __init__(self, name, sign):
        self.name = name  # player's name
        self.sign = sign  # player's sign O or X
    def get_sign(self):
        return self.sign
    def get_name(self):
        return self.name
    def choose(self, board):
        done = False
        while not(done):
            userInput = str(input(f'\n{self.get_name()}, {self.get_sign()}: Enter a cell [A-C][1-3]:\n'))
            if (board.set(userInput.upper(), self.get_sign())):
                done = True
                board.isdone()
            else:
                print('You did not choose correctly.')

class AI(Player):
    def returnMove(self, i):
        move = None
        if i == 0:
            move = 'A'+str(1)
        elif i == 1:
            move = 'B'+str(1)
        elif i == 2:
            move = 'C'+str(1)
        elif i == 3:
            move = 'A'+str(2)
        elif i == 4:
            move = 'B'+str(2)
        elif i == 5:
            move = 'C'+str(2)
        elif i == 6:
            move = 'A'+str(3)
        elif i == 7:
            move = 'B'+str(3)
        elif i == 8:
            move = 'C'+str(3)
        return move
    
    def choose(self, board):
        print(f"{self.get_name()}, {self.get_sign()}: Enter a cell [A-C][1-3]: ")
        done = False
        #randomly choose spaces until an open space is chosen
        while not(done):
            AIInput = chr(randint(ord("A"), ord("C"))) + str(int(randint(1,3)))
            if (board.set(AIInput, self.get_sign())):
                print(AIInput)
                done = True
                board.isdone()
            else:
                pass

class SmartAI(AI):
    def choose(self, board):
        print(f"{self.get_name()}, {self.get_sign()}: Enter a cell [A-C][1-3]: ")
        cell = self.hueristic(board)
        print(cell)
        board.set(cell, self.sign)

    def checkHueristicScore(self, board):
        # check the win conditions
        if board.isdone():
            if board.get_winner() == self.get_sign():
                return 1
            elif board.get_winner() == "":
                return 0
            else:
                return -1
        return 0
    
    def hueristic(self, board):
        #checks the board if the apponent can win
        for i in range(board.get_size() * board.get_size()):
            if board.get_board(i) == " ":
                if self.get_sign() == "O":
                    board.setNoCheck(i,"X")
                else:
                    board.setNoCheck(i,"O")
                score = self.checkHueristicScore(board)
                board.setNoCheck(i," ")
                if score == -1:
                    #if the ai can still win even if the apponent is able to
                    for k in range(board.get_size() * board.get_size()):
                        if board.get_board(k) == " ":
                            board.setNoCheck(k, self.get_sign())
                            score = self.checkHueristicScore(board)
                            board.setNoCheck(k," ")
                            if score == 1:
                                # correct format for move
                                return self.returnMove(k)
                    #if the apponent can win and the ai can't, the ai will block the opponent's winning space
                    return self.returnMove(i)

                elif score == 0:
                    #if the apponent can't win, the ai will check if it can win
                    for j in range(board.get_size() * board.get_size()):
                        if board.get_board(j) == " ":
                            board.setNoCheck(j, self.get_sign())
                            score = self.checkHueristicScore(board)
                            board.setNoCheck(j," ")
                            if score == 1:
                                # correct format for move
                                return self.returnMove(j)

        opponent = ''
        if self.get_sign() == "O":
            opponent = 'X'
        else:
            opponent = 'O'

        #first move will be in the middle if the ai can, if not, the ai will check many certain cases of the opponent
        #to block instances where there are 2 winning spaces for the apponent
        if board.get_board(4) == " ":
            return self.returnMove(4)
        elif board.get_board(1) == opponent and board.get_board(3) == opponent:
            if board.get_board(0) == " ":
                return self.returnMove(0)
        elif board.get_board(1) == opponent and board.get_board(5) == opponent:
            if board.get_board(2) == " ":
                return self.returnMove(2)
        elif board.get_board(5) == opponent and board.get_board(7) == opponent:
            if board.get_board(8) == " ":
                return self.returnMove(8)
        elif board.get_board(3) == opponent and board.get_board(7) == opponent:
            if board.get_board(6) == " ":
                return self.returnMove(6)
        elif board.get_board(0) == " ":
            return self.returnMove(0)
        elif board.get_board(2) == " ":
            return self.returnMove(2)
        elif board.get_board(6) == " ":
            return self.returnMove(6)
        elif board.get_board(8) == " ":
            return self.returnMove(8)
        else:
            done = False
            #randomly choose spaces until an open space is chosen
            while not(done):
                AIInput = chr(randint(ord("A"), ord("C"))) + str(int(randint(1,3)))
                if (board.set(AIInput, self.get_sign())):
                    done = True
                    return AIInput

class MiniMax(AI):
    def choose(self, board):
        print(f"{self.get_name()}, {self.get_sign()}: Enter a cell [A-C][1-3]: ")
        cell = self.findBestMoveMIniMax(board)
        print(cell)
        board.set(cell, self.sign)

    def minimax(self, board, isPlayer):
        # check the base conditions
        if board.isdone():
            if board.get_winner() == self.get_sign():
                return 1
            elif board.get_winner() == "":
                return 0
            else:
                return -1
                
        # Checking best possible move
        if isPlayer:
            bestScore = float('-inf')
            for i in range(board.get_size() * board.get_size()):
                if board.get_board(i) == " ":
                    board.setNoCheck(i,self.get_sign())
                    score = self.minimax(board,False)
                    board.setNoCheck(i," ")
                    bestScore = max(score, bestScore)
            return bestScore
        else:
            bestScore = float('inf')
            for i in range(board.get_size() * board.get_size()):
                if board.get_board(i) == " ":
                    if self.get_sign() == "O":
                        board.setNoCheck(i,"X")
                    else:
                        board.setNoCheck(i,"O")
                    score = self.minimax(board,True)
                    board.setNoCheck(i," ")
                    bestScore = min(score, bestScore)
            return bestScore

    def findBestMoveMIniMax(self, board):
        maxScore = float('-inf')
        bestMove = None
        for i in range(board.get_size() * board.get_size()):
            if board.get_board(i) == " ":
                board.setNoCheck(i,self.get_sign())
                score = self.minimax(board, False)
                board.setNoCheck(i," ")
                if score > maxScore:
                    maxScore = score
                    # correct format for move
                    bestMove = self.returnMove(i)

        return bestMove