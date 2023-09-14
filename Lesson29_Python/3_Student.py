class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades

    def calculate_average_grade(self):
        if len(self.grades) > 0:
            average_grade = sum(self.grades) / len(self.grades)
            return average_grade
        else:
            return 0

    def get_student_status(self):
        average_grade = self.calculate_average_grade()
        if average_grade >= 4.5:
            return "Excellent"
        elif average_grade >= 3.5:
            return "Good"
        else:
            return "C grade"

student1 = Student("Ivanoy Ivan", 20, [4.5, 4.0, 4.8, 4.2, 4.6])
student2 = Student("Petroy Petr", 19, [3.7, 3.8, 3.2, 3.5, 4.0])
student3 = Student("Sidaray Sidr", 21, [2.8, 3.0, 2.5, 2.9, 3.1])

print(f"{student1.name}, age: {student1.age}, average grade: {student1.calculate_average_grade()}, status: {student1.get_student_status()}")
print(f"{student2.name}, age: {student2.age}, average grade: {student2.calculate_average_grade()}, status: {student2.get_student_status()}")
print(f"{student3.name}, age: {student3.age}, average grade: {student3.calculate_average_grade()}, status: {student3.get_student_status()}")