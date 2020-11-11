import itertools #TEMP: library for getting subarrays of arrays - Combinations
from solvable_group_of_pieces import SolvableGroupOfPieces #function which run non-brute-force algs to check if pieces are solvable

def PieceCombinations(pieces, size):  #returns all combinations of size: size, from all possible pieces
    solvablPieceCombinations = []
    for pieceCombination in itertools.combinations(pieces, size):
        if SolvableGroupOfPieces(pieceCombination) == True:
            for piece in pieceCombination:
                piece.position = pieceCombination.index(piece)
            solvablPieceCombinations.append(pieceCombination)
    return solvablPieceCombinations




