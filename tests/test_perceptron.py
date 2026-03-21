from model.perceptron import AND


def test_AND_0_0():
    assert AND(0, 0) == 0


def test_AND_1_0():
    assert AND(1, 0) == 0


def test_AND_0_1():
    assert AND(0, 1) == 0


def test_AND_1_1():
    assert AND(1, 1) == 1
