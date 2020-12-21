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
                                "pos": counter
                        }
                        counter += 1
                elif (i in bars):
                        thisdict = {
                                "index": i,
                                "value": "|",
                                "type": "struct",
                                "pos": None
                        }
                else:
                        bases.append(i)
                        thisdict = {
                                "index": i,
                                "value": "___",
                                "type": "base",
                                "pos": None
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

def updatePosition(board, position):
        for i in range(len(board)):
                if (board[i]["pos"] == position):
                        print("I am here in "+str(position))
                        board[i]["value"] = "X "
        return board


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
        playerOneMove = int(input("\n"+player1+" please choose position: "))
        board = updatePosition(board, playerOneMove)
        printBoard(board)