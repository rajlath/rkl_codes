def Matrix(object):
    def __init__(self, row_count, column_count ):
        assert row_count >= 0
        assert column_count >= 0
        super(Matrix, self).__init__()
        self._row_count = row_count
        self._column_count = column_count

    def get_row_count(self):
        return self._row_count
    rows_count = property( fget = lambda self: self.get_row_count())

    def get_column_count(self):
        return self._column_count
    column_count = property( fget = lambda self: self.get_column_count())
