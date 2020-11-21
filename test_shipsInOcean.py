import pytest
from shipsInOcean import *

def test_hasShip():

    A = (0,0)
    B = (3,3)
    C = (3,1)
    D = (0,2)
    E = (0,3)
    
    assert hasShip(A, B) == True
    assert hasShip(A, C) == False
    assert hasShip(A, E) == False
    assert hasShip(E, B) == True
    assert hasShip(C, B) == True
    assert hasShip(D, B) == True
    assert hasShip(D, C) == True

def test_countShips():

    A = (0,0)
    B = (3,3)
    C = (3,1)
    D = (0,2)
    E = (0,3)

    assert countShips(A, B) == 3
    assert countShips(A, C) == 0
    assert countShips(A, E) == 0
    assert countShips(E, B) == 2
    assert countShips(C, B) == 1
    assert countShips(D, B) == 3
    assert countShips(D, C) == 1
    