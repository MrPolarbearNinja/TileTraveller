
curentPlace = "11"
forbitenRouts = "nwse"

def update_place(move, curentPlace):
    if move == "n":
        curentPlace = str(int(curentPlace) + 1)
    elif move == "e":
        curentPlace = str(int(curentPlace) + 10)
    elif move == "s":
        curentPlace = str(int(curentPlace) - 10)
    elif move == "w":
        curentPlace = str(int(curentPlace) - 1)
    return curentPlace


def printPosibleDirections (placement):
    posible = ""
    writeLine = "You can travel: "
    
    if not(placement[1] == "3"):
        if not(placement[0] == "2" and placement[1] == "2"):
            writeLine += "(N)orth "
            posible += "n"
    if not(placement[0] == "3"):
        if not(placement[0] == "1" and placement[1] == "1"):
            if not(placement[0] == "2" and placement[1] == "2"):
                if not(placement[0] == "2" and placement[1] == "1"):
                    writeLine += "(E)ast "
                    posible += "e"
    if not(placement[1] == "1"):
        if not(placement[0] == "2" and placement[1] == "3"):
            writeLine += "(S)outh "
            posible += "s"
    if not(placement[0] == "1"):
        if not(placement[0] == "2" and placement[1] == "1"):
            if not(placement[0] == "3" and placement[1] == "1"):
                if not(placement[0] == "3" and placement[1] == "2"):
                    writeLine += "(W)east "
                    posible += "w"
    print(writeLine)
    updateForbiten(posible)

def updateForbiten(fb_list):
    forbitenRouts = fb_list
def checkForbiden(WhatToCheck):
    if(forbitenRouts.find(WhatToCheck) > 0):
        return False
    return True


while (True):
    printPosibleDirections(curentPlace)

    direction = input("Direction: ")
    direction = direction.lower()

    if not(direction == "n" or direction == "e" or direction == "s" or  direction == "w"):
        print("Not a valid direction!")
    else:
        if not(checkForbiden(direction)):
            print("Not a valid direction!")
        else:
            print("NEXT MOVE")
            curentPlace = update_place(direction, curentPlace)
            
                      
