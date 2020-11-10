import itertools #library for getting subarrays of arrays - Combinations
from solvable_group_of_pieces import SolvableGroupOfPieces

def PieceCombinations(pieces):
    solvablPieceCombinations = []
    for pieceCombination in itertools.combinations(pieces, 4):
        if SolvableGroupOfPieces(pieceCombination) == True:
            for piece in pieceCombination:
                piece.position = pieceCombination.index(piece)
            solvablPieceCombinations.append(pieceCombination)
    return solvablPieceCombinations




