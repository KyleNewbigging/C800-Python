class Student:
    def __init__(self,firstName,lastName,grade):
        self.firstName = firstName
        self.lastName = lastName
        self.grade = grade
    def __str__(self):
        return self.firstName+"-"+self.lastName+" "+str(self.grade)


fObj = open("Challenge63.txt","r")
lines = fObj.readlines()
fObj.close()
list = []
for line in lines:
    firstName = line[0:line.index("-")]
    lastName = line[line.index("-")+1:line.index(" ")]
    grade = int(line[line.index(" ")+1:len(line)].rstrip())
    student = Student(firstName,lastName,grade)
    print(student)
    list.append(student)

#print(list)
option=0
while option!=6:
    option = int(input("What would you like to know\n1) The average grade\n2) Top 3 performing students\n3) List of students failing\n4) Add student and grade\n5) Update score\n6) Exit\n"))
    if option == 1:
        sum=0
        studentCount=0
        for x in list:
            sum+=x[2]
            studentCount+=1
        print("The average grade is: "+str(sum/studentCount))

    elif option == 2:
        if len(list)>3:
            list.sort() 
            for x in range(3):
                print(list[x])
        else:
            print(list)
    elif option == 3:
        print("Failing Students:")
        for x in list:
            if x.grade < 50:
                print(x)

    elif option == 4:
        firstName = input("Enter student's first name:")
        lastName = input("Enter student's last name:")
        grade = int(input("Enter student's grade"))
        student = Student(firstName,lastName,grade)
        list.append(student)

    elif option == 5:
        firstName = input("Enter student's first name:")
        grade = int(input("Enter the updated grade"))
        for x in list:
            if(firstName == x.firstName):
                x.grade = x

    elif option == 6:
        print("Good bye")

    else:
        print("Invalid input!")

#write to file
fObj = open("Challenge63.txt","w")

for student in list:
    fObj.write(str(student)+"\n")
fObj.close()