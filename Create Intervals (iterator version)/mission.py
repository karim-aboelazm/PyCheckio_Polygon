def create_intervals(data):
    left = [x for x in data if x - 1 not in data]
    right = [x for x in data if x + 1 not in data]
    return list((sorted(left), sorted(right)))

if __name__ == '__main__':

    res = create_intervals(iter(sorted(list({1, 2, 3, 4, 5, 7, 8, 12}))))
    assert hasattr(res, '__iter__'), "your function should return the iterator object"
    assert hasattr(res, '__next__'), "your function should return the iterator object"

    assert list(create_intervals(iter(sorted(list({1, 2, 3, 4, 5, 7, 8, 12}))))) == [
                                                 (1, 5), (7, 8), (12, 12)], "First"
    assert list(create_intervals(iter(sorted(list({1, 2, 3, 6, 7, 8, 4, 5}))))) == [
                                                 (1, 8)], "Second"
    print('Almost done! The only thing left to do is to Check it!')
