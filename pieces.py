from piece_class import Piece
from jigsaw import IteratePieceCombinations

def GetPieces(): #Returns all pieces for specific puzzle
    return [ #top, right, bot, left (clockwise)
            Piece(0,0,0,0), #0
            Piece(0,0,0,1), #1
            Piece(0,0,0,-1), #2
            Piece(0,0,1,1), #3
            Piece(0,0,-1,-1), #4
            Piece(0,0,1,-1), #5
            Piece(0,0,-1,1) #6    
            ]

def FindSolutions(): #Finds solutions from jigsaw
    IteratePieceCombinations(GetPieces())

FindSolutions()