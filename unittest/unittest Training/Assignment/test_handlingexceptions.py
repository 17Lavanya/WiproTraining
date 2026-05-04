import pytest

def get_element(my_list, index):
    return my_list[index]
def test_index_error():
    my_list = [1, 2, 3]
    with pytest.raises(IndexError):
        get_element(my_list, 10)
