pos = [0, 2, 4, 8, 10, 12, 16, 18, 20]
bars = [1, 3, 9, 11, 17, 19]
bases = []
def makeBoard():
        data = []
        counter = 1
        for i in range(21):
                if (i in pos):
                        thisdict = {
                                "index": i,
                                "type": "pos",
                                "value": "  ",
                                "pos": counter,
                                "marked": False
                        }
                        counter += 1
                elif (i in bars):
                        thisdict = {
                                "index": i,
                                "value": "|",
                                "type": "struct",
                                "pos": None,
                                "marked": None
                        }
                else:
                        bases.append(i)
                        thisdict = {
                                "index": i,
                                "value": "___",
                                "type": "base",
                                "pos": None,
                                "marked": None
                        }
                
                data.append(thisdict)
        return data

def printBoard(data):
        for i in range(len(data)):
                if (i == 4 or i == 7 or i == 12 or i == 15):
                        print(data[i]["value"], end="\n")
                else:
                        print(data[i]["value"], end="")


def checkMovementStatus(data):
        for i in range(len(data)):
                if i in pos:
                        if not data[i]["value"]:
                                return False
                        else:
                                return True

def updatePosition(board, position, player):
        for i in range(len(board)):
                if (board[i]["pos"] == position):
                        if not board[i]["marked"]:
                                if (player == 1):
                                        board[i]["value"] = "X "
                                else:
                                        board[i]["value"] = "O "
                                board[i]["marked"] = True
                                printBoard(board)
                        else:
                                print("This item has already been marked")
                                if (player == 1):
                                        playerOneMoveFunc(board)
                                else:
                                        playerTwoMoveFunc(board)
        return board


def playerOneMoveFunc(board):
        playerOneMove = int(input("\n"+player1+" please choose position: "))
        if (playerOneMove < 10):
                updatePosition(board, playerOneMove, 1)
        else:
                print("This position does not exist in the board")
                playerOneMoveFunc(board)

def playerTwoMoveFunc(board):
        playerTwoMove = int(input("\n"+player2+" please choose position: "))
        if (playerTwoMove < 10):
                updatePosition(board, playerTwoMove, 2)
        else:
                print("This position does not exist in the board")
                playerTwoMoveFunc(board)
        

print("Welcome to Tic Tac Toe!")
print("\n\n\n")
board = makeBoard()
# print(board)
printBoard(board)
print("\n\n\n")
print("\nThere are 2 players in this game. \n Player 1 marks X and player 2 marks O \n Do not cheat. Enjoy!")
player1 = input("Please provide player 1 name: ")
player2 = input("Please provide player 2 name: ")
while(True):
        playerOneMoveFunc(board)
        playerTwoMoveFunc(board)