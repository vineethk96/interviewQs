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

    shipCount = 0

    if hasShip(coord1, coord2):     # Are ships here?
        print("ship exists")

        if coord1 != coord2:        # The coordinates are not the same

            # Are the coordinates adjacent to each other?
            if coord1[0] + 1 == coord2[0] and coord1[1] + 1 == coord2[1]:

                # Check the smallest box
                shipCount = countShips(coord1, coord1) + shipCount
                shipCount = countShips((coord1[0], coord2[1])) + shipCount
                shipCount = countShips((coord2[0], coord1[1])) + shipCount
                shipCount = countShips(coord2, coord2) + shipCount

            elif coord1[0] + 1 == coord2[0] or coord1[1] + 1 == coord2[1]:

                # Horizontally or Vertically adjacent
                shipCount = countShips(coord1, coord1) + shipCount
                shipCount = countShips(coord2, coord2) + shipCount

            else:

                # Make more boxes
                diffx = int((coord2[0] - coord1[0])/2)
                diffy = int((coord2[1] - coord1[1])/2)

                halfCoord = (coord1[0] + diffx, coord1[1] + diffy)

                if coord1[0] == coord2[0]:          # Row Case
                    shipCount = countShips(coord1, halfCoord) + shipCount
                    shipCount = countShips((halfCoord[0] + 1, halfCoord[1]), coord2) + shipCount

                elif coord1[1] == coord2[1]:      # Column Case

                    shipCount = countShips(coord1, halfCoord) + shipCount
                    shipCount = countShips((halfCoord[0], halfCoord[1] + 1), coord2) + shipCount

                else:                                                     # Rectangle Case
                    # Find the other key Coordinates
                    q1 = ((halfCoord[0] + 1, halfCoord[1] + 1), (coord2[0], coord2[1]))
                    q2 = ((coord1[0], halfCoord[1] + 1), (halfCoord[0], coord2[1]))
                    q3 = ((coord1[0], coord1[1]), (halfCoord[0], halfCoord[1]))
                    q4 = ((halfCoord[0] + 1, coord1[1]), (coord2[0], halfCoord[1]))

                    # Break section into smaller chunks
                    shipCount = countShips(q3[0], q3[1]) + shipCount    # Quadrant 3
                    shipCount = countShips(q1[0], q1[1]) + shipCount    # Quadrant 1
                    shipCount = countShips(q2[0], q2[1]) + shipCount    # Quadrant 2
                    shipCount = countShips(q4[0], q4[1]) + shipCount    # Quadrant 4

        elif coord1 == coord2:      # The coordinates are the same
            print("Ship found!")
            shipCount = shipCount + 1

    else:                           # No Ship found
        print("No ships here")

    return shipCount


def main():
    print( str( hasShip( (0,0), (3,3) ) ))
    print( str( hasShip( (0,3), (3,3) ) ))
    print( str( hasShip( (0,0), (0,3) ) ))
    print( str( hasShip( (3,3), (0,0) ) ))

    print( str(countShips((0,3), (3,3))))





if __name__ == "__main__":
    main()