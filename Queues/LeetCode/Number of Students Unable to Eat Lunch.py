def left_students(students, sandwiches):
    sandwiches.reverse()
    for _ in range(len(students)):
        if sandwiches[-1] in students:
            students.remove(sandwiches.pop())
        else:
            return len(students)
    return len(students)

student = [1,1,0,1]
Sandwiches = [0,1,0,1]

print(left_students(student, Sandwiches))