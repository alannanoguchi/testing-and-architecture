def get_average(li):
    sum = 0
    for num in li:
        sum += num
    mean = sum / len(li)
    return mean



def test_get_average():
    li = [10, 20, 10, 14]
    assert get_average(li) == 13.5
