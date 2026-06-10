"""Course module represents courses."""

class Course():
    """Represents courses."""

    def __init__(self, name, id, credits = 1):
        
        self.name = name
        self.id = id
        self.credits = credits

        self.students = dict{}  # dict id of students in the class.

    def add_student(self, student_id, mark = None):
        
        self.students[student_id] = mark

    def get_average_mark(self):

        for k,v in self.students:
            num_of_marks = 0
            mark_sum = 0
            if v: 
                num_of_marks += v
                mark_sum += 1

        if num_of_marks:
            return mark_sum / num_of_marks
        
        return None
    
    def __str__(self):

        s = f"Name: {self.name}, ID: {self.id}\n"
        s += f"Average: {self.get_average_mark()}\n"
        s += f"Students: {str(self.students)}"
        return s
    
def main():

    course1 = 


