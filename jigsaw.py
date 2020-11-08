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

pieceStock = pieces #pieces we remove while running

#temporary array for storing board configurations while solving
tempConfig = []

solves = [] #finalized solves

removedPieces = [] #stores the removed pieces in order



#should iterate through a picked piece and all its rotations
def BoardConfigs():
    
###########################################################################
    if Piece.Sum != 0:
        return print('This combination of jigsaws has no solution')
###########################################################################
    for piece in pieceStock:
        print("once through this loop")
        for rotatedPiece in piece.RotatedVersions():
            LegalPosition(rotatedPiece, piece)
       
        try:
            rotatedPiece.append(removedPieces.pop(-1)) # adds the previously removed piece
        except IndexError:
            None 

#check if this position is legal if it is continue searching through BoardConfigs
def LegalPosition(testPiece, originPiece):
    print("WOWOWO")
    if len(tempConfig) == 0:
        if testPiece.top == testPiece.left == 0:
            tempConfig.append(testPiece) #if it is a legal move add it to board
            removedPieces.append(originPiece)
            originPiece = "used"
            BoardConfigs()
    elif len(tempConfig) == 1:
        if testPiece.top == testPiece.right == 0 and -tempConfig[0].right == testPiece.left:
            tempConfig.append(testPiece) #if it is a legal move add it to board
            removedPieces.append(originPiece)
            originPiece = "used"
            BoardConfigs()
    elif len(tempConfig) == 2:
        if testPiece.left == testPiece.bot == 0 and -tempConfig[0].bot == testPiece.top:
            tempConfig.append(testPiece) #if it is a legal move add it to board
            removedPieces.append(originPiece)
            originPiece = "used"
            BoardConfigs()
    elif len(tempConfig) == 3:
        if testPiece.bot == testPiece.right == 0 and -tempConfig[1].bot == testPiece.top and -tempConfig[2].right == testPiece.left:
            tempConfig.append(testPiece) #if it is a legal move add it to board
            #SaveSolve()
    else:
        print("piece doesnt fit")

#BoardConfigs()

for piece in tempConfig:
    print(piece.top)
    print(piece.right)
    print(piece.bot)
    print(piece.left)
    print(" ")



#we cant delete an elemen while running for elemen in list - we need to change the value instead
test = [1,2,3,4]
for element in test:
    print(element)
    if element == 1:
        #test.pop(0)
        test[0] = 'used'
#print(test)


#stuff = [1, 2, 3, 4, 5]
#for L in range(0, len(stuff)+1):
#    for subset in itertools.combinations(stuff, 4):
#        print(subset)

def returnAllPieceCombos():
    for i in range(len(pieces)):
        for pieceCombo in itertools.combinations(pieces, 4):
            print(pieceCombo)

returnAllPieceCombos()












