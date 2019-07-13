class Sinabro:
    def __init__(self, name, grade, part):
        self.name = name
        self.grade = grade
        self.part = part

    def name1(self):
        return self.name

    def grade1(self):
        return self.grade

    def part1(self):
        return self.part


a = Sinabro("세준 키임", 1, "붙이기")
print(a.name1())
print(a.grade1())
print(a.part1())
