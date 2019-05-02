class BirthdayCandy():
    def mostCandy(self, nb_student, candies):
        maxs = 0
        nb_student += 1
        for i in candies:
            maxs = max(maxs, i // nb_student + i % nb_student)
        return maxs

print(BirthdayCandy().mostCandy(4, [43, 81, 17, 1, 9]))