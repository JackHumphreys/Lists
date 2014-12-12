name1 = str(input("Please enter the name of the first student: "))
name2 = str(input("Please enter the name of the second student: "))
name3 = str(input("Please enter the name of the third student: "))
name4 = str(input("Please enter the name of the fourth student: "))
name5 = str(input("Please enter the name of the fifth student: "))
name6 = str(input("Please enter the name of the sixth student: "))
name7 = str(input("Please enter the name of the seventh student: "))
name8 = str(input("Please enter the name of the eighth student: "))

studentlist = [name1,name2,name3,name4,name5,name6,name7,name8]
selection = 1

while selection != 0:
    print()
    print("New List:")
    for count in range(8):
        print("{0}.{1}".format(count+1,studentlist[count]))
    print("0.Exit Program")

    print()
    selection = int(input("Please select a student to edit: "))

    print()
    studentlist[selection-1] = str(input("Please enter their new name: "))
