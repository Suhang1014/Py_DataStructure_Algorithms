class Array:
    def __init__(self, capacity: int):
        self.data = []
        self.capacity = capacity

    def __getitem__(self, ind: int):
        return self.data[ind]

    def __setitem__(self, ind: int, val: object):
        self.data[ind] = val
    
    def __len__(self):
        return len(self.data)

    def __iter__(self):
        '''迭代'''
        for item in self.data:
            yield item
    
    def find(self, ind: int):
        try:
            return self.data[ind]
        except IndexError:
            return None
    
    def delete(self, ind: int):
        try:
            self.data.pop(ind)
            return True
        except IndexError:
            return False

    def insert(self, ind: int, val: int):
        if len(self) >= self.capacity:
            return False
        else:
            return self.data.insert(ind, val)

    def print_all(self):
        for item in self:
            print(item)


def test_array():
    array = Array(5)
    array.insert(0, 3)
    array.insert(0, 4)
    array.insert(1, 5)
    array.insert(3, 9)
    array.insert(3, 10)
    assert array.insert(0, 100) is False
    assert len(array) == 5
    assert array.find(1) == 5
    assert array.delete(4) is True
    array.print_all()


if __name__ == "__main__":
    test_array()