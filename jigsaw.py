import itertools #combinations

class Piece(): #Class for each jigsaw puzzle piece
    def __init__(self,t,r,b,l): #initilize it with the four values for each edges indentation
        self.top = t
        self.right = r
        self.bot = b
        self.left = l

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
pieces = [#top, right, bot, left (clockwise)
         Piece(0,0,0,0), #0
         Piece(0,0,0,1), #1
         Piece(0,0,0,-1), #2
         Piece(0,0,1,1), #3
         Piece(0,0,-1,-1), #4
         Piece(0,0,1,-1), #5
         Piece(0,0,-1,1) #6    
         ]

#temporary array for storing board configurations while solving
tempConfig = []

solves = [] #finalized solves

#should iterate through a picked piece and all its rotations
def BoardConfigs(pieceStock):
    
    for piece in pieceStock:
        print("once through this loop")
        for rotatedPiece in piece.RotatedVersions():
            LegalPosition(rotatedPiece, piece, pieceStock)
        tempConfig.pop()

#check if this position is legal if it is continue searching through BoardConfigs
def LegalPosition(testPiece, originPiece, pieceStock):
    print("WOWOWO")
    if len(tempConfig) == 0:
        if testPiece.top == testPiece.left == 0:
            tempConfig.append(testPiece) #if it is a legal move add it to board
            pieceStock.remove(originPiece) #removes item from list
            BoardConfigs(pieceStock) #calls function with now new shortened list
    elif len(tempConfig) == 1:
        if testPiece.top == testPiece.right == 0 and -tempConfig[0].right == testPiece.left:
            tempConfig.append(testPiece) #if it is a legal move add it to board
            pieceStock.remove(originPiece) #removes item from list
            BoardConfigs(pieceStock) #calls function with now new shortened list
    elif len(tempConfig) == 2:
        if testPiece.left == testPiece.bot == 0 and -tempConfig[0].bot == testPiece.top:
            tempConfig.append(testPiece) #if it is a legal move add it to board
            pieceStock.remove(originPiece) #removes item from list
            BoardConfigs(pieceStock) #calls function with now new shortened list
    elif len(tempConfig) == 3:
        if testPiece.bot == testPiece.right == 0 and -tempConfig[1].bot == testPiece.top and -tempConfig[2].right == testPiece.left:
            tempConfig.append(testPiece) #if it is a legal move add it to board
            SaveSolve() #temp save solve where it just prints
    else:
        print("piece doesnt fit")

def SaveSolve():
    for piece in tempConfig:
        print(piece.top)
        print(piece.right)
        print(piece.bot)
        print(piece.left)
        print(" ")



def FindPossiblePieceCombinations():
    for pieceCombo in itertools.combinations(pieces, 4):
        sum = 0
        for piece in pieceCombo:
            sum += piece.Sum()
        if sum == 0
            BoardConfigs(pieceCombo)













