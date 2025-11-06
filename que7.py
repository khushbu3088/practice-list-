'''7. Write a Python program to print the numbers of a specified list after removing
even numbers from it.'''
li=[20,34,35,55,57,59]
new_li=[]
for i in li:
 if i%2!=0:
     new_li.append(i)
print(new_li)
 
