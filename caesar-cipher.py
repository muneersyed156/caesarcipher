import string
print("Enter the plain text")
a=str(input())
print("Enter key value: ")
k=int(input())
e=''
d=''
for i in a:
    if(i.islower() and i.isalpha()):
        e=e+chr((((ord(i)+k)-ord('a'))%26)+ord('a'))
    elif(i.isupper() and i.isalpha()):
        e=e+chr((((ord(i)+k)-ord('A'))%26)+ord('A'))
    else:
        e=e+i
print("The cipher text generated is "+e)

for i in e:
    if(i.islower() and i.isalpha()):
        d=d+chr((((ord(i)-k)-ord('a'))%26)+ord('a'))
    elif(i.isupper() and i.isalpha()):
        d=d+chr((((ord(i)-k)-ord('A'))%26)+ord('A'))
    else:
        d=d+i
print("The plain text converted is"+d)