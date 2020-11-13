# Imagine an ocean where ships are marked with the char x.
# You are provided a function hasShip(a, b) which accepts tuples
# This function returns a boolean on if a ship exists within 
# the two coordinates.

# Goal: create a function countShips(a, b) which leverages 
# hasShip to determine the amount of ships in the ocean.

'''
|E|x|x|A|
---------
| |C| |x|
---------
| | | |D|
---------
|B| | | |
'''
# (0,0) is in the bottom left corner
# A = (3,3)
# B = (0,0)
# C = (1,2)
# D = (3,1)
# E = (0,3)


# hasShip(A, C) = True
# hasShip(A, D) = True
# hasShip(E, B) = False
# hasShip(D, B) = 

# Global Variables
shipCount = 0

def hasShip(coord1, coord2):

    x1 = (1,3)
    x2 = (2,3)
    x3 = (3,2)

    if x1[0] >= coord1[0] and x1[0] <= coord2[0] and x1[1] >= coord1[1] and x1[1] <= coord2[1]:
        return True    
    elif x2[0] >= coord1[0] and x2[0] <= coord2[0] and x2[1] >= coord1[1] and x2[1] <= coord2[1]:
        return True
    elif x3[0] >= coord1[0] and x3[0] <= coord2[0] and x3[1] >= coord1[1] and x3[1] <= coord2[1]:
        return True
    else:
        return False


def countShips(coord1, coord2):

    if hasShip(coord1, coord2) and coord1 != coord2:

        diffx = coord2[0] - coord1[0]
        diffy = coord2[1] - coord1[1]
        
        halfCoord = (coord1[0] + diffx, coord1[1] + diffy)
        leftCoord = (coord1[0], halfCoord[1])
        topCoord = (halfCoord[0], coord2[1])
        rightCoord = (coord2[0], halfCoord[1])
        bottomCoord = (halfCoord[0], coord1[1])
        
        countShips(coord1, halfCoord)       # Quadrant 3
        countShips(halfCoord, coord2)       # Quadrant 1
        countShips(leftCoord, topCoord)     # Quadrant 2
        countShips(bottomCoord, rightCoord) # Quadrant 4

    elif hasShip(coord1, coord2) and coord1 == coord2:
        shipCount = shipCount + 1

    else:
        print("No ships here")

    return shipCount


def main():
    print( str( hasShip( (0,0), (3,3) ) ))
    print( str( hasShip( (0,3), (3,3) ) ))
    print( str( hasShip( (0,0), (0,3) ) ))
    print( str( hasShip( (3,3), (0,0) ) ))

    print( str(countShips((0,0), (3,3))))





if __name__ == "__main__":
    main()