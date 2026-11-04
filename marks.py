print("STUDENT MARKS MANAGEMENT")
name = input("Enter student name: ")
mark1 = int(input("Enter Linux marks: "))
mark2 = int(input("Enter AWS marks: "))
mark3 = int(input("Enter Git marks: "))
mark4 = int(input("Enter Python marks:"))
total = mark1 + mark2 + mark3 + mark4
average = total / 4
print("\n----- STUDENT RESULT -----")
print("Student Name:", name)
print("Linux Marks:", mark1)
print("AWS Marks:", mark2)
print("Git Marks:", mark3)
print("Python Marks:", mark4)
print("Total Marks:", total)
print("Average:", average)
if mark1 >= 35 and mark2 >= 35 and mark3 >= 35 and marks4 >= 35:    
      print("Result: PASS")
else:    
     print("Result: FAIL") 
            
print("Thank you for using Student Marks Management") 
