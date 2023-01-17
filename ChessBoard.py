import numpy as np
from Move import Move
from Utils import *
import time
from sys import exit
import pygame
class ChessBoard:

    def __init__(self):

        self.board = np.zeros((8,8),dtype = int)
        self.pieceEaten = []
        self.listOfMove = []
        self.whiteTurn = True

        self.board[0,0] = 4
        self.board[1,0] = 2
        self.board[2,0] = 3
        self.board[3,0] = 5
        self.board[4,0] = 6
        self.board[5,0] = 3
        self.board[6,0] = 2
        self.board[7,0] = 4
        self.board[0,7] = -4
        self.board[1,7] = -2
        self.board[2,7] = -3
        self.board[3,7] = -5
        self.board[4,7] = -6
        self.board[5,7] = -3
        self.board[6,7] = -2
        self.board[7,7] = -4

        for i in range(8):
            self.board[i,1] = 1
            self.board[i,6] = -1

        self.moveAvailable = None




    def checkMove(self):
        return(True)
        # Check for a candidatemove if the king is in danger or not
        
    def isLegal(self,move):
        allMoves = self.getAllMove()
        isLegal = False
        for m in allMoves:
            if(m.equal(move)):
                isLegal = True
                
        return(isLegal)

    def getAllMove(self):
        listOfMove = []
        multiplier = -1
        if(self.whiteTurn):
            multiplier = 1
        for i in range(8):
            for j in range(8):
                numero = self.board[i,j]*multiplier

                if(numero == 1):
                    m = self.getPawnMove(i,j)
                    listOfMove = listOfMove + m

                if(numero == 2):
                    m = self.getKnightMove(i,j)
                    listOfMove = listOfMove + m

                if(numero == 3):
                    m = self.getBishopMove(i,j)
                    listOfMove = listOfMove + m

                if(numero == 4):
                    m = self.getRookMove(i,j)
                    listOfMove = listOfMove + m

                if(numero == 5):
                    m = self.getQueenMove(i,j)
                    listOfMove = listOfMove + m

                if(numero == 6):
                    m = self.getKingMove(i,j)
                    listOfMove = listOfMove + m

        return(listOfMove)

    def makeMove(self,move):
        i,j,k,l = move.i,move.j,move.k,move.l
        clock = pygame.time.Clock()
        multiplier = -1
        if(self.whiteTurn):
            multiplier = 1
        spec = move.spec
        
        legal = self.isLegal(move)
        if(not legal):
            spec = "not legal"
            print("Erreur coup illégal")
            
            move.show()
            
            clock.tick(0.1)
            
        if(spec == "None" or spec == "Pawn"):
            self.pieceEaten.append(self.board[k,l])
            self.board[k,l] = self.board[i,j]
            self.board[i,j] = 0
            self.whiteTurn = not self.whiteTurn
            self.listOfMove.append(move)

        if(spec == "Rook"):
            self.pieceEaten.append(self.board[k,l])
            self.board[k,l] = 4 * multiplier
            self.board[i,j] = 0
            self.whiteTurn = not self.whiteTurn
            self.listOfMove.append(move)

        if(spec == "Knight"):
            self.pieceEaten.append(self.board[k,l])
            self.board[k,l] = 2 * multiplier
            self.board[i,j] = 0
            self.whiteTurn = not self.whiteTurn
            self.listOfMove.append(move)

        if(spec == "Bishop"):
            self.pieceEaten.append(self.board[k,l])
            self.board[k,l] = 3 * multiplier
            self.board[i,j] = 0
            self.whiteTurn = not self.whiteTurn
            self.listOfMove.append(move)

        if(spec == "Queen"):
            self.pieceEaten.append(self.board[k,l])
            self.board[k,l] = 5 * multiplier
            self.board[i,j] = 0
            self.whiteTurn = not self.whiteTurn
            self.listOfMove.append(move)

        if(spec == "En passant"):
            print("== EN PASSANT")
            self.pieceEaten.append(self.board[k,j])
            self.board[k,l] = multiplier
            self.board[i,j] = 0
            self.board[k,j] = 0
            self.whiteTurn = not self.whiteTurn
            self.listOfMove.append(move)
            
    

    def unmakeMove(self):
        # Assume last move exist
        n = len(self.listOfMove)
        if (n== 0):
            pygame.quit()
            exit()
            
        previousMove = self.listOfMove[n-1]
        
      
        piece = self.pieceEaten[n-1]
        i,j,k,l = previousMove.i,previousMove.j,previousMove.k,previousMove.l
        self.board[i,j] = self.board[k,l]
        if(previousMove.spec == "En passant"):
            self.board[k,j] = piece
            self.board[k,l] = 0
        else :
            self.board[k,l] = piece
            
        self.pieceEaten.pop(n-1)
        self.listOfMove.pop(n-1)
        self.whiteTurn = not self.whiteTurn
    


    def inBound(self,i,j):
        #check if given coordinate are in bound
        return(0 <= i and i <=7 and 0<= j and j <= 7)



    def getPawnMove(self,i,j):
        #Get the pawn movement for the pawn located in i, j
        # We assume coordinate are correct

        multiplier = -1
        listOfMove = []
        if(self.whiteTurn):
            multiplier = 1

        # check for moving forward
        if(self.board[i,j+multiplier] == 0):
            if(1 <= j+multiplier and j+multiplier <= 6):
                move = Move(i,j,i,j+multiplier, "None")
                listOfMove.append(move)

            else :
                move = Move(i,j,i,j+multiplier, "Queen")
                listOfMove.append(move)
                move = Move(i,j,i,j+multiplier, "Knight")
                listOfMove.append(move)
                move = Move(i,j,i,j+multiplier, "Rook")
                listOfMove.append(move)
                move = Move(i,j,i,j+multiplier, "Bishop")
                listOfMove.append(move)

        # check moving forward two square
        if(j == 1 and self.whiteTurn):
            if(self.board[i,2] == 0 and self.board[i,3] == 0):
                move = Move(i,1,i,3,"Pawn")
                listOfMove.append(move)
                # Means that pawn moved forward two case for en passant


        if(j == 6 and not self.whiteTurn):
            if(self.board[i,5] ==0 and self.board[i,4] == 0):
                move = Move(i,6,i,4,"Pawn")
                listOfMove.append(move)


        # check for captures
        if (inBound(i+1,j+multiplier)):
            if(self.board[i+1,j+multiplier]*multiplier < 0):
                if(1 <= j+multiplier and j+multiplier <= 6):
                    move = Move(i,j,i+1,j+multiplier, "None")
                    listOfMove.append(move)
                else :
                    move = Move(i,j,i+1,j+multiplier, "Queen")
                    listOfMove.append(move)
                    move = Move(i,j,i+1,j+multiplier, "Knight")
                    listOfMove.append(move)
                    move = Move(i,j,i+1,j+multiplier, "Rook")
                    listOfMove.append(move)
                    move = Move(i,j,i+1,j+multiplier, "Bishop")
                    listOfMove.append(move)

        if (inBound(i-1,j+multiplier)):
            if(self.board[i-1,j+multiplier]*multiplier < 0):

                if(1 <= j+multiplier and j+multiplier <= 6):
                    move = Move(i,j,i-1,j+multiplier, "None")
                    listOfMove.append(move)
                else :
                    move = Move(i,j,i-1,j+multiplier, "Queen")
                    listOfMove.append(move)
                    move = Move(i,j,i-1,j+multiplier, "Knight")
                    listOfMove.append(move)
                    move = Move(i,j,i-1,j+multiplier, "Rook")
                    listOfMove.append(move)
                    move = Move(i,j,i-1,j+multiplier, "Bishop")
                    listOfMove.append(move)





        # check for en passant (TO DO)
        if (len(self.listOfMove) > 0):
            previousMove = self.listOfMove[len(self.listOfMove)-1]
            if (previousMove.spec =="Pawn"):
                if (abs(i-previousMove.i) == 1 and j == previousMove.l ):
                    move = Move(i,j,previousMove.i,j+ multiplier,"En passant")
                    listOfMove.append(move)

        return(listOfMove)

    def getKnightMove(self,i,j):
        #Get the pawn movement for the pawn located in i, j
        #We assume coordinate are correct

        multiplier = -1
        listOfMove = []
        if(self.whiteTurn):
            multiplier = 1

        candidate = getKnightSquare(i,j)
        for c in candidate:
            if(self.board[c[0],c[1]]*multiplier <= 0):
                move = Move(i,j,c[0],c[1],"None")
                listOfMove.append(move)

        return(listOfMove)

    def getRookMove(self,i,j):

        multiplier = -1
        listOfMove = []
        if(self.whiteTurn):
            multiplier = 1

        direction = [[1,0],[-1,0],[0,1],[0,-1]]

        for dir in direction:
            continuer = True
            x = i
            y = j
            while continuer:

                xf,yf = x+dir[0],y+dir[1]
                if (inBound(xf,yf) and self.board[xf,yf]*multiplier <= 0):
                    move = Move(i,j,xf,yf,"None")
                    listOfMove.append(move)
                    if(self.board[xf,yf]*multiplier  < 0 ):
                        continuer = False
                    else:
                        x,y = xf,yf
                else :
                    continuer = False

        return(listOfMove)

    def getBishopMove(self,i,j):

        multiplier = -1
        listOfMove = []
        if(self.whiteTurn):
            multiplier = 1

        direction = [[1,1],[-1,1],[1,-1],[-1,-1]]

        for dir in direction:
            continuer = True
            x = i
            y = j
            while continuer:

                xf,yf = x+dir[0],y+dir[1]
                if (inBound(xf,yf) and self.board[xf,yf]*multiplier  <= 0):
                    move = Move(i,j,xf,yf,"None")
                    listOfMove.append(move)
                    if (self.board[xf,yf]*multiplier  < 0):
                        continuer = False
                    else :
                        x,y = xf,yf
                else :
                    continuer = False
        return(listOfMove)

    def getQueenMove(self,i,j):
        return(self.getRookMove(i,j) + self.getBishopMove(i,j))

    def getKingMove(self,i,j):
        multiplier = -1
        listOfMove = []
        if(self.whiteTurn):
            multiplier = 1
        for x in range(i-1,i+2):
            for y in range(j-1,j+2):
                if(inBound(x,y) and self.board[x,y] *multiplier <= 0):
                    move = Move(i,j,x,y,"None")
                    listOfMove.append(move)

        return(listOfMove)


    def addPiece(self,i,j,val):
        self.board[i,j] = val

    def show(self):
        print(self.board)
        
    def score(self):
        score = 0
        for i in range(8):
            for j in range(8):
                n = self.board[i][j]
                if(n == 1):
                    score += 1
                    score += 0.1*(j-1)
                if(n == 2):
                    score += 3
                if(n == 3):
                    score += 3
                if(n == 4):
                    score += 5
                if(n == 5):
                    score += 9
                if(n == 6):
                    score += 1000
                if(n == -1):
                    score -= 1
                    score += 0.1*(j-7)
                if(n == -2):
                    score -= 3
                if(n == -3):
                    score -= 3
                if(n == -4):
                    score -= 5
                if(n == -5):
                    score -= 9
                if(n == -6):
                    score -= 1000
        return(score)
    
    
