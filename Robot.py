from ChessBoard import ChessBoard
import random as rd
class Robot:

    def __init__(self,chessboard):
        self.game = chessboard



    def minMax(self,currentProfondeur,alpha, beta):

        if (currentProfondeur == 3):
            return([],self.game.score())
        else:
            whiteTurn = self.game.whiteTurn
            bestMove = []
            continuer = True
            if(whiteTurn):
                s = -10000
            else:
                s = 10000

            moves = self.game.getAllMove()

            rd.shuffle(moves)
            if(whiteTurn):
                self.tri(moves,1)
            else :
                self.tri(moves,-1)

            if(len(moves) > 0):
                bestMove = moves[0]
            else:
                print("Pas de coup")

            for m in moves :
                self.game.makeMove(m)
                move,score = self.minMax(currentProfondeur+1,alpha,beta)

                    
                    
                self.game.unmakeMove()
                if (whiteTurn):
                    if(score > alpha):
                        bestMove = m
                        alpha = score
                        s = score

                else :
                    if(score < beta):
                        bestMove = m
                        beta = score
                        s = score


                if(beta < alpha):
                    break

            if(currentProfondeur == 0):
                print("Best move")
                print(m)
            return(bestMove,s)


    def computeMove(self):
        whiteTurn = self.game.whiteTurn
        bestMove,s = self.minMax(0,-100000,100000)
        print(bestMove)
        self.game.makeMove(bestMove)

    def makeMove(self,m):
        self.game.makeMove(m)


    def tri(self,moves,c):
        scores =[]
        for m in moves :
            """print("Show move")
            m.show()
            print("Move Shown")"""
            n = len(self.game.listOfMove)
            print(n)
            print("Making move")
            self.game.makeMove(m)
            scores.append(self.game.score())
            n = len(self.game.listOfMove)
            print(n)
            print("Unmaking move")
            self.game.unmakeMove()

        for i in range(len(moves)):
            for j in range(len(moves)-i-1):
                if (scores[j]*c < scores[j+1]*c):
                    scores[j],scores[j+1]= scores[j+1],scores[j]
                    moves[j],moves[j+1]= moves[j+1],moves[j]