#9. Write a Python program to find the second largest number in a list.
li=[2,3,4,5,6,7,6,7]
m=max(li)
new_li=[]
for i in li:
    if i==m:
        pass
    else:
        new_li.append(i)
print(new_li)
new_li.sort()
print(new_li[-1])
    

