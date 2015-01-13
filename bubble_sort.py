
def input_list():
    unordered = []
    finished = False
    while not finished:
        item = input("Please enter an item: ")
        if item == "stop":
            finished = True
        else:
            unordered.append(item)
    return unordered

def bubble_sort(unordered_list):
    finished = False
    while finished == False:
        for item in range(len(unordered_list)-1):
            if unordered_list[item] > unordered_list[item+1]:
                temp = unordered_list[item] 
                unordered_list[item] = unordered_list[item+1]
                unordered_list[item+1] = temp
                print(unordered_list)
            finished == True
                   
unordered_list = input_list()
bubble_sort(unordered_list)
    
