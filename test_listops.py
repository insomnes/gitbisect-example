import listops as lo


def test_remove_duplicates():
    print('Running remove_duplicates tests')
    inp = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
    out = lo.remove_duplicates(inp)
    for i in inp:
        assert out.count(i) == 1


    assert lo.remove_duplicates([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert lo.remove_duplicates([1, 1, 1, 1, 1]) == [1]
    assert lo.remove_duplicates([1, 2, 3, 1, 2, 3]) == [1, 2, 3]
    assert lo.remove_duplicates([1, 1, 2, 2, 22, 22, 3, 4, 5]) == [1, 2, 22, 3, 4, 5]


if __name__ == '__main__':
    print('Running tests')
    test_remove_duplicates()
    print('All tests passed')
