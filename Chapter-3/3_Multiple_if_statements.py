# If elif else ladder
a = int(input())

# If statement : 1
if(a%2 == 0):
    print("Even")

# End of If statement : 1  
#  
# If statement : 2   
if(a >= 18):
    print("The person is adult")
elif(a < 0):
    print("Age of the person is invalid")
elif(a == 0):
    print("Age is 0 , which is invalid") 
else:
    print("The person is not adult")   

# End of If statement : 2
print("End of the program")     

