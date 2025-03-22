"""
Create a StudentRecord class that accepts the name of a student and their marks in three subjects as arguments in the constructor. Then, implement a method to calculate and print the average marks of the student. Additionally, include a static method that converts marks from percentages to a grade based on the following criteria:

90-100: A
80-89: B
70-79: C
60-69: D
Below 60: F
"""
class StudentRecord:
    def __init__(self, name, subject):
        self.name= name
        self.subject = subject
        
    def  calcaverage(self):
        
        avg= sum(self.subject)/len(self.subject)
        print(f"The mark of {self.name} is {avg:.2f}")
        return avg
    @staticmethod
    def grade( marks):
        if marks >= 90 and marks <= 100:  
            return 'A'  
        elif marks >= 80:  
            return 'B'  
        elif marks >= 70:  
            return 'C'  
        elif marks >= 60:  
            return 'D'  
        else:  
            return 'F' 

student1= StudentRecord("Me",[80,80,80])
average= student1.calcaverage()
GPA = student1.grade(average)
print(f"The result of {student1.name} is : {GPA} ")
