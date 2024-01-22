slices = int(input("Enter the TOTAL number of SLICES:"))
numStudents = int(input("Enter the number of students:"))
slicesPerPerson = int(slices/numStudents)
extraSlices = slices%numStudents
print("Each person gets "+str(slicesPerPerson)+". There will be "+str(extraSlices)+" extra slice(s)")
