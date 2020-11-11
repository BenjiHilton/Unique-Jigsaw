from piece_class import Piece                       #class defining each jigsaw piece used in puzzle
from piece_combinations import PieceCombinations    #import a function returning all possible ways you can combine a group of pieces
from save_solution import PrintSolution             #TEMP: function for printing solution - GOAL: will later save it

solves = []         #finalized solves
usedPieces = []     #keeps track of used pieces in current branch (ROTATION SPECIFIC)
removedPieces = []  #keeps track of removed pieces (ORIGIN PIECE)

def IteratePieceCombinations(pieces):   #go through each combination of pieces to look for solves
    for pieceCombination in PieceCombinations(pieces, 4): #TEMP: 4 - size of current puzzle 2x2
        CreateBoardConfig(pieceCombination)

def CreateBoardConfig(pieceStock):  #BAD NAME? Recursive function - for each piece and its rotation check if the rotated piece fits
    for piece in pieceStock:        #until puzzle is filled then call SaveSolve and search through all possible permutations
        if piece.position > -1:     #check if the piece has been used already
            for rotatedPiece in piece.RotatedVersions():
                if(PlaceablePiece(rotatedPiece)):           #if the piece fits in current board configuration
                    usedPieces.append(rotatedPiece)         #add the rotated piece to the current board configuration
                    removedPieces.append(piece)             #remember that the piece has been removed(order specific)
                    piece.position = -piece.position - 1    #set the position-val to negative so it cant be used again
                    if(len(usedPieces) < 4):                #if it is not the final piece:
                        CreateBoardConfig(pieceStock)       #Start recursion - call same function for the next piece
                    else:                                   #else save solution and climb back up tree
                        PrintSolution(usedPieces)           
                        removedPiece = removedPieces.pop(-1)
                        removedPiece.position = -removedPiece.position - 1
                        usedPieces.pop(-1)    
    if(removedPieces != []):    #climb back up on tree
        removedPiece = removedPieces.pop(-1)    
        removedPiece.position = -removedPiece.position - 1 #set position back to positive so it can be used again
        usedPieces.pop(-1)

def PlaceablePiece(tryPiece): #returns true/false based on if argument(piece) can be placed in puzzle
    if ((len(usedPieces) == 0 and tryPiece.top == tryPiece.left == 0) #first piece
    or (len(usedPieces) == 1 and tryPiece.top == tryPiece.right == 0 and -usedPieces[0].right == tryPiece.left) #second piece
    or (len(usedPieces) == 2 and tryPiece.left == tryPiece.bot == 0 and -usedPieces[0].bot == tryPiece.top) #third piece
    or (len(usedPieces) == 3 and tryPiece.bot == tryPiece.right == 0 and -usedPieces[1].bot == tryPiece.top and -usedPieces[2].right == tryPiece.left)): #fourth piece
        return True
    else:
        return False
