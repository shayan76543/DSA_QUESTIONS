from collections import deque
def unableStudent(students: list[int], sandwishes: list[int]) -> int:
    students = deque(students)
    rotation = 0
    top = 0
    while top<len(sandwishes):
        if students[0] == sandwishes[top]:
            students.popleft()
            top += 1
            rotation = 0
        else:
            student = students.popleft()
            students.append(student)
            rotation += 1
            if rotation >= len(students):
                return len(students)
    return len(students)
print(unableStudent(students=[0, 1, 0, 1, 0, 1],sandwishes=[0, 0, 0, 0, 1, 1]))
