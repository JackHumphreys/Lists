result = 0
index = 0
value = [24,13,57,45]
finished = False
while not finished:
    index = index + 1
    if result < value[index]:
        result = value[index]
    if index == 4:
        finished = True
print(result)

