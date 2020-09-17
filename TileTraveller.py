curentPlace = "12"

def printPosibleDirections (placement):

    writeLine = "You can travel: "
    if not(placement[1] == "3"):
        if not(placement[0] == "2" and placement[1] == "2"):
            writeLine += "(N)orth "
    if not(placement[0] == "3"):
        if not(placement[0] == "1" and placement[1] == "1"):
            if not(placement[0] == "2" and placement[1] == "2"):
                if not(placement[0] == "2" and placement[1] == "1"):
                    writeLine += "(E)ast "
    if not(placement[1] == "1"):
        if not(placement[0] == "2" and placement[1] == "3"):
            writeLine += "(S)outh "
    if not(placement[0] == "1"):
        if not(placement[0] == "2" and placement[1] == "1"):
            if not(placement[0] == "3" and placement[1] == "1"):
                if not(placement[0] == "3" and placement[1] == "2"):
                    writeLine += "(W)east "
    print(writeLine)
printPosibleDirections(curentPlace)