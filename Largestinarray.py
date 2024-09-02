import numpy as np
n=int(input("enter the size of array"))
l=[]
for i in range(n):
    e=int(input("enter element"))
    l.append(e)
print(l)
find=int(input("enter which largest no must be found in aray"))
sort=np.sort(l)
new=np.flip(sort)
print(new)
print(f"the {find}th largest element in array is",new[find-1])

