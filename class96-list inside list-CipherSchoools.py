# list inside list 
matrix=[[1,2,3],[4,5,6],[7,8,9]] #2d list 
print(matrix[0])
for sublist in matrix:
    for i in sublist:
        print(i)
# axcessing list inside list by index 
print(matrix[2][1])

# type 
print(type(matrix))


