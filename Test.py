from ChessBoard import ChessBoard
from Robot import Robot
from Move import Move

def Test():
    chess = ChessBoard()
    #chess.addPiece(4,4,3)

    chess.show()

    moves = chess.getAllMove()
    print("Affichage des coups")
    print("Il y a " + str(len(moves)))
    for m in moves:
        m.show()
    print("Done")
    print("*******")
    m = Move(0,1,0,3,"Pawn")
    chess.makeMove(m)
    
    
    chess.show()
    moves = chess.getAllMove()
    print("Affichage des coups")
    print("Il y a " + str(len(moves)))
    for m in moves:
        m.show()
    print("Done")
    print("*******")
    m = Move(7,6,7,4,"Pawn")
    chess.makeMove(m)
    
    chess.show()
    moves = chess.getAllMove()
    print("Affichage des coups")
    for m in moves:
        m.show()
    print("Done")
    print("Il y a " + str(len(moves)) + " coup")
    print("*******")
    m = Move(0,3,0,4,"None")
    chess.makeMove(m)
    
    
    chess.show()
    moves = chess.getAllMove()
    print("Affichage des coups")
    for m in moves:
        m.show()
    print("Done")
    print("Il y a " + str(len(moves)) + " coup")
    print("*******")
    m = Move(1,6,1,4,"Pawn")
    chess.makeMove(m)
    
    
    
    chess.show()
    moves = chess.getAllMove()
    print("Affichage des coups")
    for m in moves:
        m.show()
    print("Done")
    print("Il y a " + str(len(moves)) + " coup")
    print("*******")
    m = Move(0,4,1,5,"En passant")
    chess.makeMove(m)
    
    chess.show()
    chess.unmakeMove()
    chess.show()
    
Test()
    
    
    
    