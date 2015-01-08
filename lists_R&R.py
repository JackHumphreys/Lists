#Lists for R&R

def name_input():
    students = []
    for count in range(8):
        name = str(input("Please input student name: "))
        students.append(name)
    return students




def list_edit(studentlist):
    selection = 1
    while selection != 0:
        print()
        print("New List:")
        for count in range(8):
            print("{0}.{1}".format(count+1,studentlist[count]))
        print("0.Exit Program")

        print()
        selection = int(input("Please select a student to edit: "))
        if selection > 0:
            print()
            studentlist[selection-1] = str(input("Please enter their new name: "))



studentlist = name_input()
list_edit(studentlist)
