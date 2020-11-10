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


