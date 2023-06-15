class FlatIterator:

    def __init__(self, list_of_list):
        self.local_list = list_of_list

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        self.index += 1
        count = 0
        for i in range(len(self.local_list)):
            for j in range(len(self.local_list[i])):
                count += 1
                if count == self.index:
                    return self.local_list[i][j]
        raise StopIteration


def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()