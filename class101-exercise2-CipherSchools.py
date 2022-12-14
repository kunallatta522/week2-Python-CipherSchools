# by reverse 
def reverse_list(l):
    l.reverse()
    return l
number=[1,2,3,4]
print(reverse_list(number))

# by append and  pop 
def reverse_list(l):
    r_list=[]
    for i in range(len(l)):
        poppeditem=l.pop()
        r_list.append(poppeditem)
    return r_list


