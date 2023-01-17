def inBound(i,j):
    #check if given coordinate are in bound
    return(0 <= i and i <=7 and 0<= j and j <= 7)

def getKnightSquare(i,j):
    res = []
    candidate = [[i+1,j+2],[i+1,j-2],[i-1,j+2],[i-1,j-2],[i+2,j+1],[i+2,j-1],[i-2,j+1],[i-2,j-1]]
    for c in candidate:
        if(inBound(c[0],c[1])):
            res.append(c)
    return(res)







