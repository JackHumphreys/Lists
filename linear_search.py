def linear_search_input():
    searchlist = []
    finished = True
    while not finished == True:
        item = input("Please enter item in list (stop to finish list): ")
        searchlist.append(item)
        if item == -1:
            search = input("Please enter search term: ")
    return searchlist,search
        

def linear_search(search_list,search_term):
    found = False
    count = 0
    while not found and count < len(search_list):
        if search_list[count] == search_term:
            print("Found")
            found = True
        else:
            print("Not found")
        count = count + 1
        

search_list,search_term = linear_search_input()

