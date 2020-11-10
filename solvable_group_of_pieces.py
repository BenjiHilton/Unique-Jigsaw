def SolvableGroupOfPieces(groupOfPieces):
    sum = 0
    for piece in groupOfPieces:
        sum += piece.Sum()
    return True if sum == 0 else False

