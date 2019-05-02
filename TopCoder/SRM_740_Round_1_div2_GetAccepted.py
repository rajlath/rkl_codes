class GetAccepted():
    def answer(self, string):
        strings = [x for x in string.split()]
        not_count = strings.count("not")
        return ["False", "True"][not_count % 2 == 0]


print(GetAccepted().answer("Do you not want to not get not not not accepted?"))