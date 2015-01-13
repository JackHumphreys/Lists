def linear_search_input():
    searchlist = []
    finished = False
    while not finished:
        item = input("Please enter item in list (stop to finish list): ")
        if item == "stop":
            finished = True
        else:
            searchlist.append(item)
    find = input("Please enter search term: ")
    return searchlist,find
        

def linear_search(search_list,search_term):
    found = False
    count = 0
    while not found and count < len(search_list):
        if search_list[count] == search_term:
            print("Found at list value {0}".format(count+1))
            found = True
        else:
            pass
        count = count + 1
        return
        

search_list,search_term = linear_search_input()
linear_search(search_list,search_term)
