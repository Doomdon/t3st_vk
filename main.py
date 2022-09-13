import pytest


#float


@pytest.mark.parametrize("test_input,expected", [("2.2+4", 6.2)])
def test_float_1(test_input, expected):
    assert eval(test_input) == expected


@pytest.mark.parametrize("test_input,expected", [("2.2+4", 6)])
def test_float_negative(test_input, expected):
    try:
        assert eval(test_input) == expected
    except AssertionError:
        pass

#str
def func_str(x,y):
    return str(x) + str(y)


def test_str_1():
    assert func_str(1, 2) == '12'


def test_str_negative():
    try:
        assert func_str(1, 2) == 3
    except AssertionError:
        pass



#dict

def test_dict_1():
    assert {'a': {'b': 2, 'c': {'d': 4}}} == {'a': {'b': 2, 'c': {'d': 4}}}

def test_dict_2():
    a = {
        "name": "Andrew",
        "location": "Russia",
        "size": "huge",
    }
    b = {
        "name": "Ivan",
        "location": "Water",
        "size": "huge",
    }
    assert a != b
