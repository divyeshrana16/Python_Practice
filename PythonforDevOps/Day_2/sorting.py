list_of_num = [1,2,3,4,5,6,-7,-5,-4,-3,-1]

for i in range(len(list_of_num)):
    for j in range(len(list_of_num)):
        if list_of_num[i] < list_of_num[j]:
            temp = list_of_num[i]
            list_of_num[i] = list_of_num[j]
            list_of_num[j] = temp

print(list_of_num)