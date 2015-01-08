import random

def start_list():
    mylist = []
    for count in range(1,20):
        mylist.append(count)
    return mylist

def random_select(full_list):
    choice_list = []
    finished = False
    while finished != True:
        choice = random.choice(full_list)
        if choice != 0:
            choice_list.append(choice)
            print(choice)
            full_list.pop(choice-1)
            full_list.insert(choice-1,0)
        else:
            pass
        if len(choice_list) == 6:
            finished = True
    return choice_list, full_list
        
#Main

full_list = start_list()

rand_choice,final_list = random_select(full_list)

print()
print(rand_choice)
print()
print(final_list)
