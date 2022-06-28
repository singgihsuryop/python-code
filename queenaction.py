# Tested Code
class Test :
    @staticmethod
    def main( args) :
        Test.solution("5 3", "4 3", ["5 5", "4 2", "2 3"])
    @staticmethod
    def solution( n_k,  qPos,  oPos) :
        boardSize = int(n_k.split(" ")[0])
        numOfObstacle = int(n_k.split(" ")[1])
        queenRowPos = int(qPos.split(" ")[0])
        queenColPos = int(qPos.split(" ")[1])
        pin = [[0] * (boardSize) for _ in range(boardSize)]
        pin[queenRowPos][queenColPos] = 1
        for o in oPos :
            pin[int(o.split(" ")[0]) - 1][int(o.split(" ")[1]) - 1] = -1
        counter = 1
        i = 0
        while (i < 8) :
            counter = 1
            if (i==0):
                # up
                while (queenRowPos + counter < boardSize) :
                    if (pin[queenRowPos + counter][queenColPos] == 0) :
                        pin[queenRowPos + counter][queenColPos] = 1
                    else :
                        break
                    counter += 1
            elif(i==1):
                # up right
                while (queenRowPos + counter < boardSize and queenColPos + counter < boardSize) :
                    if (pin[queenRowPos + counter][queenColPos + counter] == 0) :
                        pin[queenRowPos + counter][queenColPos + counter] = 1
                    else :
                        break
                    counter += 1
            elif(i==2):
                # right
                while (queenColPos + counter < boardSize) :
                    if (pin[queenRowPos][queenColPos + counter] == 0) :
                        pin[queenRowPos][queenColPos + counter] = 1
                    else :
                        break
                    counter += 1
            elif(i==3):
                # down right
                while (queenRowPos - counter <= 0 and queenColPos + counter < boardSize) :
                    if (pin[queenRowPos - counter][queenColPos + counter] == 0) :
                        pin[queenRowPos - counter][queenColPos + counter] = 1
                    else :
                        break
                    counter += 1
            elif(i==4):
                # DOWN
                while (queenRowPos - counter <= 0) :
                    if (pin[queenRowPos - counter][queenColPos] == 0) :
                        pin[queenRowPos - counter][queenColPos] = 1
                    else :
                        break
                    counter += 1
            elif(i==5):
                # down left
                while (queenRowPos - counter <= 0 and queenColPos - counter <= 0) :
                    if (pin[queenRowPos - counter][queenColPos - counter] == 0) :
                        pin[queenRowPos - counter][queenColPos - counter] = 1
                    else :
                        break
                    counter += 1
            elif(i==6):
                # left
                while (queenColPos - counter <= 0) :
                    if (pin[queenRowPos][queenColPos - counter] == 0) :
                        pin[queenRowPos][queenColPos - counter] = 1
                    else :
                        break
                    counter += 1
            elif(i==7):
                # up left
                while (queenRowPos + counter < boardSize and queenColPos - counter <= 0) :
                    if (pin[queenRowPos + counter][queenColPos - counter] == 0) :
                        pin[queenRowPos + counter][queenColPos - counter] = 1
                    else :
                        break
                    counter += 1
            i += 1
        countQueenMove = 0
        row = 0
        while (row < boardSize) :
            col = 0
            while (col < boardSize) :
                countQueenMove = countQueenMove + pin[row][col]
                col += 1
            row += 1
        countQueenMove = countQueenMove + numOfObstacle
        print(countQueenMove)
    

if __name__=="__main__":
    Test.main([])
