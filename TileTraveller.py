curentPlace = "32"

def printPosibleDirections (placement):
    print("You can travel: ")
    if not(placement[1] == "3"):
        if not(placement[0] == "2" and placement[1] == "2"):
            print("(N)orth")
    if not(placement[0] == "3"):
        if not(placement[0] == "1" and placement[1] == "1"):
            if not(placement[0] == "2" and placement[1] == "2"):
                if not(placement[0] == "2" and placement[1] == "1"):
                    print("(E)ast")
    if not(placement[1] == "1"):
        if not(placement[0] == "2" and placement[1] == "3"):
            print("(S)outh")
    if not(placement[0] == "1"):
        if not(placement[0] == "2" and placement[1] == "1"):
            if not(placement[0] == "3" and placement[1] == "1"):
                if not(placement[0] == "3" and placement[1] == "2"):
                    print("(W)east")
printPosibleDirections(curentPlace)