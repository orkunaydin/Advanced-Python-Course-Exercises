class Person():
    def __init__(self, first_name, last_name):
        self.full_name = first_name + " " + last_name
    def getName(self):
        return self.full_name

class Student(Person):
    def __init__(self, first_name, last_name, subject):
        super(Student, self).__init__(first_name, last_name)
        self.subject = subject
    def printNameSubject(self):
        self.NameSubject = self.full_name + ", " + self.subject
        return self.NameSubject

class Teacher(Person):
    def __init__(self, first_name, last_name, course):
        super(Teacher, self).__init__(first_name, last_name)
        self.course = course
    def printNameCourse(self):
        self.NameCourse = self.full_name + ", " + self.course
        return self.NameCourse
