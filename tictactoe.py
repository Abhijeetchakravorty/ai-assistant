import itertools 
from itertools import combinations, chain
pos = [0, 2, 4, 8, 10, 12, 16, 18, 20]
possub = [{0, 2, 4}, {8, 10, 12}, {16, 18, 20}, {0, 8, 16}, {2, 10, 18}, {4, 12, 20}, {0, 10, 20}, {4, 10, 16}]
bars = [1, 3, 9, 11, 17, 19]
def findsubsets(s, n): 
        return list(map(set, itertools.combinations(s, n))) 
def makeBoard():
        data = []
        counter = 1
        for i in range(21):
                if (i in pos):
                        thisdict = {
                                "index": i,
                                "value": "  ",
                                "pos": counter,
                                "marked": False
                        }
                        counter += 1
                elif (i in bars):
                        thisdict = {
                                "index": i,
                                "value": "|",
                                "pos": None,
                                "marked": None
                        }
                else:
                        thisdict = {
                                "index": i,
                                "value": "___",
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
                                        playerOneMoveFunc(board, player)
                                else:
                                        playerTwoMoveFunc(board, player)
        return board
def playerOneMoveFunc(board, player1):
        playerOneMove = int(input("\n"+str(player1)+" please choose position: "))
        if (0 != playerOneMove < 10):
                updatePosition(board, playerOneMove, 1)
        else:
                print("This position does not exist in the board")
                playerOneMoveFunc(board, player1)
def playerTwoMoveFunc(board, player2):
        playerTwoMove = int(input("\n"+str(player2)+" please choose position: "))
        if (0 != playerTwoMove < 10):
                updatePosition(board, playerTwoMove, 2)
        else:
                print("This position does not exist in the board")
                playerTwoMoveFunc(board, player2)
def checkWinner(board, player1, player2):
        notFound = True
        for i in range(len(possub)):
                a = []
                for val in possub[i]:
                        a.append(val)
                if ((a[0] is not None and a[1] is not None and a[2] is not None) and (board[a[0]]["value"] == board[a[1]]["value"] == board[a[2]]["value"] != "  ")):
                        notFound = False
                        if (board[a[0]]["value"] == "X "):
                                print()
                                print("Winner is "+str(player1))
                        else:
                                print()
                                print("Winner is "+str(player2))
                        break
        if (notFound == False):
                return True
        else:
                return False
def checkDraw(board):
        draw = False
        if (board[pos[0]]["value"] != "  " and board[pos[1]]["value"] != "  " and board[pos[2]]["value"] != "  " and board[pos[3]]["value"] != "  " and board[pos[4]]["value"] != "  " and board[pos[5]]["value"] != "  " and board[pos[6]]["value"] != "  " and board[pos[7]]["value"] != "  " and board[pos[8]]["value"] != "  "):
                draw = True
        return draw

                        
print("Welcome to Tic Tac Toe!")
print("\n\n\n")
board = makeBoard()
print(board)
printBoard(board)
print("\n\n\n")
print("\nThere are 2 players in this game. \n Player 1 marks X and player 2 marks O \n Do not cheat. Enjoy!")
player1 = input("Please provide player 1 name: ")
player2 = input("Please provide player 2 name: ")
while(True):
        playerOneMoveFunc(board, player1)
        data = checkWinner(board, player1, player2)
        if (data == True):
                break
        else:
                draw = checkDraw(board)
                if (draw):
                        print("Match is a tie")
                        break
        playerTwoMoveFunc(board, player2)
        data = checkWinner(board, player1, player2)
        if (data == True):
                break
        else:
                draw = checkDraw(board)
                if (draw):
                        print("Match is a tie")
                        break
