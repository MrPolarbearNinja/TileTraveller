curentPlace = "23"

def printPosibleDirections (placement):
    print("You can travel: ")
    if(placement[1] == "1"):
        print("(N)orth")
    if(placement[0] == "1" and not placement[1] == "1"):
        print("(E)ast")
    if not(placement[1] == "1" and (placement[0] == 2 and placement[0] == 3)):
        print("(S)outh")

printPosibleDirections(curentPlace)