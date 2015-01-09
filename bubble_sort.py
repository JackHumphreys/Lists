
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
    count = 0
    
    if unordered_list[count] > unordered_list[count+1]:
        temp = unordered_list[count] 
        unordered_list[count] = unordered_list[count+1]
        unordered_list[count+1] = temp
        print(unordered_list)
        
       
        
    
        
            
unordered_list = input_list()
bubble_sort(unordered_list)
    
