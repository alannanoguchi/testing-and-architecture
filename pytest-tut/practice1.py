import math

def get_average(li):
    if not li:
            return float('NaN')
    sum = 0
    for num in li:
        sum += num
    mean = sum / len(li)
    return mean

def test_get_average():
    assert math.isclose(get_average([1,2,3,4]), 2.5)

def test_get_average_empty_list():
    assert math.isnan(get_average([]))
