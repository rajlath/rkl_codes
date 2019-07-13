from collections import defaultdict
class School(object):
    def __init__(self):
        self.classes = defaultdict(list)

    def add_student(self, name, grade):
        if grade in self.classes:
            self.classes[grade].append(name)
        else:
            self.classes[grade] = [name]

    def roster(self):
        answers = []
        gclass = sorted(self.classes.keys())
        for cl in gclass:
            if cl in self.classes:
                answers += sorted(self.classes[cl])
        return answers



    def grade(self, grade_number):
        students = []
        if grade_number in self.classes:
            students = self.classes[grade_number]
        return sorted(students)

