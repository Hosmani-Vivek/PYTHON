a=int(input("enter value of a"))
b=int(input("enter value of b"))
count=0;
sum=0;
while a<=b:
    if a%2==0:
         print(a)
         count+=1
         sum+=a
    a+=1
print(sum)
print(count)
