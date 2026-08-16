'''Write a program to find out whether a student has passed or failed if it requires a total of 40% and at least 33% in each subject to pass.
 Assume 3 subjects and take marks as input from the user.'''

marks1 = int(input())
marks2 = int(input())
marks3 = int(input())
total = marks1 + marks2 + marks3
total_percentage = (total / 300)*100
if(marks1 >= 33 and marks2>= 33 and marks3 >= 33 or total_percentage >= 40):
    print("pass",total_percentage)
else:
    print("failed",total_percentage)    