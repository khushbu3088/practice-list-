'''3. Write a Python program to count the number of strings where the string length
is 2 or more and the first and last characters are same from a given list of strings.'''
li=['abc','xyz','aba','1221','a']
count=0
for i in li:
 if len(i)>=2 and i[0]==i[-1]:
  count+=1
print(count)
