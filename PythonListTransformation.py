#Task 1: Given the list of grades: Sort the grades in descending order and print the sorted list.

grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]

grades.sort()
grades.sort(reverse=True)
print(grades)

#Task 2: Calculate the average grade and print it.

numbers = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
sumOfNums = 0
count = 0
for number in numbers:
    sumOfNums += number
    count += 1
average = sumOfNums / count
print("The average grade is:", average)