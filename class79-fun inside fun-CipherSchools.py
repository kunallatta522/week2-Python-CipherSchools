def new_greatest(a,b,c):
    bigger = greater(a,b)
    return greater(bigger,c)
print(new_greatest(1,2,3))