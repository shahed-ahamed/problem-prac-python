class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        return f"My name is {self.name}."

class Student(Person):
    def __init__(self, name, student_id):
        super().__init__(name) 
        self.student_id = student_id

    def introduce(self):
        base_intro = super().introduce()
        return f"{base_intro} I am a student with ID {self.student_id}."


p1 = Person("Shahed")
s1 = Student("Shahed", "CSE65D")

print(p1.introduce())  
print(s1.introduce())
