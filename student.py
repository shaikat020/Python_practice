class Student:
    def __init__(self, name, mark1, mark2, mark3):
        self.name=name
        self.mark1= mark1
        self.mark2= mark2
        self.mark3= mark3
    def print_average(self):
        sum_mark = self.mark1+ self.mark2+self.mark3
        average = sum_mark/3
        print(f"Name : {self.name} \n ID : {average:.2f}")
student1 = Student("Abasdf", 3.00, 3.25, 2.98)
student1.print_average()