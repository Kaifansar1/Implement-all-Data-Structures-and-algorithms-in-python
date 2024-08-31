def item_in_common(list1,list2):
    for i in list1:
        for j in list2:
            if i==j:
                return True
    return False        
                               #approach 1 nested for loops --> o(n*2)
list1= [1,3,5]
list2= [2,4,32]

print(item_in_common(list1,list2))



      #approach 2 using dictionary or hash map/table --> o(n)


def items_in_common(list1, list2):
    my_dict={}
    for i in list1:
        my_dict[i]=True
    for j in list2:
        if j in my_dict:    # == or in both can be used here
            return True
    return False        

list1= [1,3,5]
list2= [2,4,5]

print(item_in_common(list1,list2))
