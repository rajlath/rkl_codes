class CopyingHomework():
    def copy(self,friendsHomework):
        my_home_work = [x - 1 for x in friendsHomework[:5]]
        my_home_work[4] += 5
        return my_home_work


print(CopyingHomework().copy([10, 20, 30, 40, 50]))


