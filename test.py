class AgeException(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return (f"age: {self.value} is not valid")
    
try:
    age = int(input("Enter your age: "))
    if age < 0 or age > 120:
        raise AgeException(age)
    print(f"Your age is: {age}")
except AgeException as e:
    print(e)
else:
    print("Age is valid.")
finally:
    print("Age validation complete")


