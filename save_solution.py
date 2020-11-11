def PrintSolution(solution): #TEMP: print the acquired solution - GOAL: save the solution
    print("##########***SOLUTION***############")
    for piece in solution:
        print(piece.top)
        print(piece.right)
        print(piece.bot)
        print(piece.left)
        print("###")