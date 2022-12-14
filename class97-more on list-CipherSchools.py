# more about list 
numbers=list(range(1,11))
print(numbers)
# removing number by pop 
numbers.pop()
print(numbers)
#popped number 
print(numbers.pop())
# value search through list (we will get index postion of value)
print(numbers.index(2))


#fun inside list
def negative_list(l):
    negative=[]
    for i in l:
        negative.append(-i)
    return negative
print(negative_list(numbers))

 