class Array(object):
    def __init__(self, length=0, base_index= 0):
        assert length >= 0
        self._data = [0]*length
        self._base_index = base_index

    def copy(self):
        result = Array(len(self._data))
        for i, dataum in enumerate(self._data):
            result._data[i] = dataum
        result._base_index = self._base_index
        return result

    def get_index_offset(self, index):
        offset = index - self._base_index
        if 0 <=  offset <= self.length - 1:
            return offset
        else: raise IndexError

    def __get_item__(self, index):
        return self._data[self.get_index_offset(index)]

    def __set_item__(self, index, value):
        self._data[self.get_index_offset(index)] = value

    def get_data(self):
        return self._data

    data = property(fget = lambda self: self.get_data())

    def get_base_index(self):
        return self._base_index

    def set_base_index(self, index):
        self._base_index = index

    base_index = property(
                            fget = lambda self:self.get_base_index(),
                            fset = lambda self:self.set_base_index(value)
                          )
    def __len__(self):
        return len(self._data)

    def set_length(self, value):
        if len(self._data) != value:
            new_data = [None for i in range(value)]
            m = min(len(self._data), value)
            for i in range(m):
                new_data[i] = self._data[i]
            self._data = new_data

    length = property (
         fget = lambda self: self.__len__(),
         fset = lambda self: self.set_length(value))



arr = Array(5)
arr1= arr.copy()
print(arr.set_length(10))
print(arr.length)
print(arr.base_index)
print(arr1.data)

