'''1) Write a program to check whether a student has passed or failed.
 The student needs at least 35 marks in each of 3 subjects and at least 40% overall.'''

mark1 = int(input())
mark2 = int(input())
mark3 = int(input())

total = mark1 + mark2 + mark3
total_percentage = (total / 300)*100

if(mark1 >= 35 and mark2 >= 35 and mark3 >=35 and total_percentage >= 40):
    print("Passed",total_percentage)
else:
    print("Failed",total_percentage)    


'''2) Write a program to check whether a student is eligible to sit for an exam. A student must have 75% or more attendance.'''

attendance = int(input())
if(attendance >= 75):
    print("Student is eligible to sit for an exam", attendance)
else:
    print("Not eligible", attendance)    

'''3) Write a program to check whether a person is eligible for a driving license.
 Take the person's age as input. The minimum age is 18.'''

age = int(input())
if(age >= 18):
    print("Person is eligible for a driving license")
else:
    print("Not eligible")   

'''4) Write a program to check whether a person is eligible to vote. Take age as input. A person must be 18 or older.'''

age1 = int(input())
if(age1 >= 18):
    print("Person is eligible to vote")
else:
    print("person is not eligible to vote")   

'''5) Scholarship Eligibility
Write a program to check whether a student is eligible for a scholarship. The student must have:

At least 80% overall marks
Family income less than ₹3,00,000 per year

Take both values as input.'''

marks = int(input())
family_income = int(input())
if(marks >= 80 and family_income <= 300000):
    print("student is eligible for a scholarship")
else:
    print("student is not eligible for a scholarship")    

'''6) Student Grade
Write a program that takes marks of 3 subjects and prints:

A → 80% or above
B → 60%–79%
C → 40%–59%
Fail → below 40% '''

mark = int(input())
if(mark >= 80):
    print("A")
elif(mark >= 60):
    print("B")
elif(mark >= 40):
    print("C")
else:
    print("Fail")   

'''7) Salary Bonus
Write a program to calculate whether an employee gets a bonus. An employee gets a bonus if:

Experience is 5 years or more, AND
Salary is less than ₹50,000

Take salary and experience as input.'''

salary = int(input())
experience_year = int(input())
if(experience_year >= 5 and salary <= 50000):
    print("Employee gets a bonus")
else:
    print("No bonus")    

'''8) Electricity Bill Category
Write a program that takes electricity units as input and prints:

Below 100 units → Low Usage
100–300 units → Medium Usage
Above 300 units → High Usage'''

electricity_unit = int(input())
if(electricity_unit <= 100):
    print("Low Usage")
elif(electricity_unit <= 300):
    print("Medium Usage")
else:
    print(" High Usage")

'''9) Three Numbers
Take three numbers as input and check whether all three numbers are positive. Print "All Positive" or "Not All Positive".'''

a = int(input())
b = int(input())
c = int(input())
if(a > 0 and b > 0 and c > 0):
    print("All Positive")
else:
    print("Not All Positive")    
