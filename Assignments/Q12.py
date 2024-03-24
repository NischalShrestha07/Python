#WAP TO READ 3 SUBJECT MARKS AND DISPLAY PASS OR FAILED USING CLASS AND OBJECT

class Student:
    def __init__(self, name):
        self.name = name
        self.marks = []

    def input_marks(self):
        for i in range(3):
            subject = input(f"Enter marks for subject {i + 1}: ")
            self.marks.append(int(subject))

    def calculate_result(self):
        total_marks = sum(self.marks)
        average_marks = total_marks / 3

        if average_marks >= 40 and all(mark >= 33 for mark in self.marks):
            return "PASS"
        else:
            return "FAILED"

    def display_result(self):
        result = self.calculate_result()
        print(f"{self.name} has {result} with an average of {sum(self.marks) / 3} marks.")

student_name = input("Enter student's name: ")
student = Student(student_name)


student.input_marks()

student.display_result()
