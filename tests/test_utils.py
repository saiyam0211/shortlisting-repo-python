from src.utils import find_max, get_first_n_items

def test_find_max_negative():
    assert find_max([-5, -2, -8]) == -2

def test_get_first_n():
    assert get_first_n_items([1,2,3,4,5], 3) == [1,2,3]
