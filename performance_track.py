def cal_average(student):
    average = {name: sum(marks) / len(marks) for name, marks in student.items()}
    top_performer = max(average, key=average.get)
    return average, top_performer

student = {"John": [85, 78, 92], "Alice": [88, 79, 95], "Bob": [70, 75, 80]}
average, top_performer = cal_average(student)
print(f"Average Marks: {average}")
print(f"Top Performer: {top_performer}")
