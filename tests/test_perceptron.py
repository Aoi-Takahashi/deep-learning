from model.perceptron import AND, NAND, OR, XOR


# (x1,x2)=(0,0)
def test_AND1():
    assert AND(0, 0) == 0


# (x1,x2)=(1,0)
def test_AND2():
    assert AND(1, 0) == 0


# (x1,x2)=(0,1)
def test_AND3():
    assert AND(0, 1) == 0


# (x1,x2)=(1,1)
def test_AND4():
    assert AND(1, 1) == 1


# (x1,x2)=(0,0)
def test_OR1():
    assert OR(0, 0) == 0


# (x1,x2)=(1,0)
def test_OR2():
    assert OR(1, 0) == 1


# (x1,x2)=(0,1)
def test_OR3():
    assert OR(0, 1) == 1


# (x1,x2)=(1,1)
def test_OR4():
    assert OR(1, 1) == 1


# (x1,x2)=(0,0)
def test_NAND1():
    assert NAND(0, 0) == 1


# (x1,x2)=(1,0)
def test_NAND2():
    assert NAND(1, 0) == 1


# (x1,x2)=(0,1)
def test_NAND3():
    assert NAND(0, 1) == 1


# (x1,x2)=(1,1)
def test_NAND4():
    assert NAND(1, 1) == 0


# (x1,x2)=(0,0)
def test_XOR1():
    assert XOR(0, 0) == 0


# (x1,x2)=(1,0)
def test_XOR2():
    assert XOR(1, 0) == 1


# (x1,x2)=(0,1)
def test_XOR3():
    assert XOR(0, 1) == 1


# (x1,x2)=(1,1)
def test_XOR4():
    assert XOR(1, 1) == 0
