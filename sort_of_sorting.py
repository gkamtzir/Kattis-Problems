# Defining a class for students.
class Student:
    def __init__(self, name, unique_id):
        self.name = name
        self.id = unique_id

# Using merge sort.
def merge_sort(students): 
    if len(students) >1: 
        mid = len(students) // 2
        L = students[:mid]  
        R = students[mid:]
  
        merge_sort(L)
        merge_sort(R)
  
        i = j = k = 0
          
        # Sorting the elements by the first 2
        # letter of students' name.
        while i < len(L) and j < len(R): 
            if L[i].name[:2] < R[j].name[:2]: 
                students[k] = L[i] 
                i += 1
            elif L[i].name[:2] > R[j].name[:2]:
                students[k] = R[j] 
                j += 1
            else:
                # If the 2 first letters are the same
                # then we sort by id.
                if L[i].id < R[j].id:
                    students[k] = L[i]
                    i += 1
                else:
                    students[k] = R[j]
                    j += 1
            k+=1
          
        # Adding the remaining elements.
        while i < len(L): 
            students[k] = L[i] 
            i += 1
            k += 1
          
        while j < len(R): 
            students[k] = R[j] 
            j += 1
            k += 1

number_of_students = int(input())

while number_of_students != 0:
    students = []
    unique_id = 0
    for i in range(number_of_students):
        name = input()
        students.append(Student(name, unique_id))
        unique_id += 1
    merge_sort(students)
    for student in students:
        print(student.name)
    print("")
    number_of_students = int(input())
