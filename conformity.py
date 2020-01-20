def get_hash(courses):
    string = ""
    for course in courses:
        string += str(course)
    return hash(string)

n = int(input())

record = {}

for i in range(n):
    courses = sorted(list(map(int, input().split())))
    courses_hash = get_hash(courses)
    if record.get(str(courses_hash)) is not None:
        record[str(courses_hash)] += 1
    else:
        record[str(courses_hash)] = 1
max_same_courses = -1
result = -1

for key, value in record.items():
    if value > max_same_courses:
        result = value
        max_same_courses = value
    elif value == max_same_courses:
        result += value
        
print(result)
