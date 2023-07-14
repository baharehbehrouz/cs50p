from bank import value
def test_hello():
    assert value("hello") == 0
    assert value("Hello") == 0

def test_h():
    assert value("h") == 20
    assert value("Hi") ==20


def test_other():
    assert value("Ciao") == 100
    assert value("what`s happining?")==100

# def test_bank():
#     assert value("Hello") == "$0"
#     assert value("Hi") == "$20"
#     assert value("Ciao") == "$100"