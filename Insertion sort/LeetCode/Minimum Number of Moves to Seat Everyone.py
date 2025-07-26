def minMovesToSeat(seats, students):
    result = 0
    seats.sort()
    students.sort()
    for i in range(len(seats)):
        result += abs(seats[i] - students[i])
    return result


seat = [3,1,5]
student = [2,7,4]

print(minMovesToSeat(seat, student))