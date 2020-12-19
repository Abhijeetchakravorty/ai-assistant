for i in range(9):
        if (i == 0 or i==1 or i==2):
                if (i == 0 or i == 1):
                        print("___|", end="")
                else:
                        print("___", end="")
        elif (i==3 or i==4 or i==5):
                if (i==3):
                        print()
                        print("___|", end="")
                if (i==4):
                        print("___|", end="")
                if (i==5):
                        print("___", end="")        
        elif (i==6 or i==7 or i==8):
                if (i==6):
                        print()
                print("___", end=" ")
        else:
                pass