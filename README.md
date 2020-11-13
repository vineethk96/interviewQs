# interviewQs
## Interview Question Practice

Imagine an ocean where ships are marked with the char x.
You are provided a function hasShip(a, b) which accepts tuples
This function returns a boolean on if a ship exists within the two coordinates.

# Goal: create a function countShips(a, b) which leverages hasShip to determine the amount of ships in the ocean.

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
