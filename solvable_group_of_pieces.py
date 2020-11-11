def SolvableGroupOfPieces(groupOfPieces):   #runs algorithms (non-brute-force) to check if the set of pieces are solvable
    sum = 0
    for piece in groupOfPieces: #ALG 1: their sum must be zero - as many indents ans extends
        sum += piece.Sum()
    return True if sum == 0 else False

