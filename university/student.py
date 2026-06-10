"""Student module for simple university example"""

class Student():
    """Represents a student with basic details."""

    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.courses = {}

    def add_course(self, course_id, mark = None):
        self.courses[course_id] = mark 

    def add_mark(self, course_id, mark):
        self.courses[course_id] = mark

    def get_gpa(self): #should return float
       # To get gpa, we have to implement weighted average.
       # Course should implement course.credit * student.course[course_id]
       for k,v in self.courses.items():
            nums = 0
            sum = 0
            if v: 
                nums += v
                sums += 1

        if nums:
            return sum / nums
        
        return None


    def __str__(self):
        s = f"Name: {self.name}, ID: {self.id}\n"
        s += f"GPA: {self.get_gpa()}\n"
        s += f"Courses: {str(self.courses)}"
        return s
    

def main():
    """This is a test function for the Student class."""

    print("test1: ")
    s1 = Student("Michelle Macharia", 1001)
    s1.add_course("B100S0320206")
    print(s1)

if __name__ == "__main__":
    main()