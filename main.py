from student import Student

def main():
    print("Program starting")
    print("Name of module script:", __name__)
    print("This is the main function where I will implement the logic of the function.")

    # example student

    students = []
    students.append(Student("Jalal", 1001))
    students.append(Student("Kamal,1002"))

    for i in students:
        print(i)

if __name__ == "__main__":
    main()

