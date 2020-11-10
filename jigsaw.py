from piece_class import Piece
from piece_combinations import PieceCombinations
from solvable_group_of_pieces import SolvableGroupOfPieces
from save_solution import PrintSolution

#define each of the 7 possible pieces for a 2x2 jigsaw puzzle
solves = [] #finalized solves
usedPieces = [] #keeping working config of board

removedPieces = [] #keeps track of removed pieces

def IteratePieceCombinations(pieces):
    for pieceCombination in PieceCombinations(pieces):
        CreateBoardConfig(pieceCombination)

def CreateBoardConfig(pieceStock):
    for piece in pieceStock:

        #print("TESTET PIECE POSITION: " + str(piece.position))
        if piece.position > -1:
            #print("TRYING THE PIECE")
            for rotatedPiece in piece.RotatedVersions():
                if(PlaceablePiece(rotatedPiece)):
                    removedPieces.append(piece)
                    usedPieces.append(rotatedPiece)
                    piece.position = -piece.position - 1
                    #print("USED PIECE POSITION: " + str(piece.position))
                    #print("###############################:  " +str(len(usedPieces)))
                    if(len(usedPieces) < 4):
                        #print("ENTERED RECURSION")
                        CreateBoardConfig(pieceStock)
                    else:
                        PrintSolution(usedPieces)
                        removedPiece = removedPieces.pop(-1)
                        removedPiece.position = -removedPiece.position - 1
                        usedPieces.pop(-1)    
    #print("DEAD END - GOING BACK UP ON TREE")
    if(removedPieces != []):
        removedPiece = removedPieces.pop(-1)
        removedPiece.position = -removedPiece.position - 1
        usedPieces.pop(-1)
        #print("ADDED BACK PIECE POSITION: " + str(removedPiece.position))


def PlaceablePiece(tryPiece):
    if ((len(usedPieces) == 0 and tryPiece.top == tryPiece.left == 0)
    or (len(usedPieces) == 1 and tryPiece.top == tryPiece.right == 0 and -usedPieces[0].right == tryPiece.left)
    or (len(usedPieces) == 2 and tryPiece.left == tryPiece.bot == 0 and -usedPieces[0].bot == tryPiece.top)
    or (len(usedPieces) == 3 and tryPiece.bot == tryPiece.right == 0 and -usedPieces[1].bot == tryPiece.top and -usedPieces[2].right == tryPiece.left)):
        return True
    else:
        #print("ROTATED PIECE DIDNT FIT")
        return False



# TESTPIECES = [Piece(0,0,1,1), #3
#          Piece(0,0,-1,-1), #4
#          Piece(0,0,1,-1), #5
#          Piece(0,0,-1,1) #6
# ]

# for piece in TESTPIECES:
#     piece.position = TESTPIECES.index(piece)
# CreateBoardConfig(TESTPIECES)
