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