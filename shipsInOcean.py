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
# hasShip(D, B) = False

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
    


def main():
    print( str( hasShip( (0,0), (3,3) ) ))
    print( str( hasShip( (0,3), (3,3) ) ))
    print( str( hasShip( (0,0), (0,3) ) ))





if __name__ == "__main__":
    main()