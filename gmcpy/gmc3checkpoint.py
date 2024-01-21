import numpy as np


num_students = int(input("Enter the number of students: "))
num_subjects = int(input("Enter the number of subjects: "))

# Create a Numpy array to store marks
marks_array = np.zeros((num_students, num_subjects))

for i in range(num_students):
    percentage = 0
    total=0
    for j in range(num_subjects):
        marks_array[i,j] = float(input(f"write the  mark n {j} of the student n {i}:  "))
    total = marks_array[i,j].sum()
    percentage=(total/(num_subjects))*100
    if percentage>=90:
        print("A+")
    elif percentage>=80:
        print("A")
    elif percentage>=70:
        print("B+")
    elif percentage>=60:
        print("B")
    elif percentage>=50:
        print("C")
    else:
        print("F")
    percentage=0
    total=0

