#4. Write a Python program to remove duplicates from a list.
li=[20,30,20,40,20]
new_li=[]
for i in li:
    if i in new_li:
        pass
    else:
        new_li.append(i)
print(new_li)        

#2 wy
li=[20,30,20,40,20]
new_li=[]
for i in li:
    if i not in new_li:
        new_li.append(i)
print(new_li)        
        


