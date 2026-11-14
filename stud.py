name = input("Enter student name: ")
no_ofsubjects = int(input("Enter number of subjects: "))
total = 0

for i in range(0, no_ofsubjects):
    marks = int(input("Enter marks: "))
    total = total + marks

print("Total marks: ",total)

avg = total / no_ofsubjects

print("Average is:",avg)

percentage = (total / (no_ofsubjects * 100)) * 100
print("Percentage is:", percentage, "%")

if percentage > 50:
    print("Result: PASS")
else:
    print("Result: FAIL")
