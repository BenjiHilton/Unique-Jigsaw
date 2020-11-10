import itertools #library for getting subarrays of arrays - combinations

class Piece(): #A jigsaw puzzle piece class
    def __init__(self,t,r,b,l): #initilize it with the four values for each edges indentation
        self.top = t
        self.right = r
        self.bot = b
        self.left = l
        self.position = None

    def Rotate(self,turns): #rotate the piece specified amount
        if turns == 1:
            return Piece(self.left, self.top, self.right, self.bot)
        elif turns == 2:
            return Piece(self.bot, self.left, self.top, self.right)
        elif turns == 3:
            return Piece(self.right, self.bot, self.left, self.top)

    def RotatedVersions(self): #return array with the different possible rotated pieces
        if self.top == self.right == self.bot == self.left:
            return [self]
        elif self.top == self.bot and self.right == self.left:
            return [self,self.Rotate(1)]
        else:
            return [self, self.Rotate(1), self.Rotate(2), self.Rotate(3)]
    
    def Sum(self):
        return (self.top + self.right + self.bot + self.left)


#define each of the 7 possible pieces for a 2x2 jigsaw puzzle
allPossiblePieces = [#top, right, bot, left (clockwise)
         Piece(0,0,0,0), #0
         Piece(0,0,0,1), #1
         Piece(0,0,0,-1), #2
         Piece(0,0,1,1), #3
         Piece(0,0,-1,-1), #4
         Piece(0,0,1,-1), #5
         Piece(0,0,-1,1) #6    
         ]

solves = [] #finalized solves

usedPieces = [] #keeping working config of board

removedPieces = [] #keeps track of removed pieces

def IteratePieceCombos():
    for pieceCombo in itertools.combinations(allPossiblePieces, 4):
        if PossiblePieceCombo(pieceCombo) == True:
            print("############***TRYING NEW PIECE COMBO***########")
            for piece in pieceCombo:
                piece.position = pieceCombo.index(piece)
            CreateBoardConfig(pieceCombo)

def PossiblePieceCombo(pieces):
    sum = 0
    for piece in pieces:
        sum += piece.Sum()
    return True if sum == 0 else False

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
                        SaveSolve(usedPieces)
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

def SaveSolve(solution):
    print("##########***SOLUTION***############")
    for piece in solution:
        print(piece.top)
        print(piece.right)
        print(piece.bot)
        print(piece.left)
        print("x")
IteratePieceCombos()

# TESTPIECES = [Piece(0,0,1,1), #3
#          Piece(0,0,-1,-1), #4
#          Piece(0,0,1,-1), #5
#          Piece(0,0,-1,1) #6
# ]

# for piece in TESTPIECES:
#     piece.position = TESTPIECES.index(piece)
# CreateBoardConfig(TESTPIECES)
