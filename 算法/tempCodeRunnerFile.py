a = '''
import sys
import math

def find1(a1,b1):
    for i in a1:
        if i == b1:
            return False
    return True

a,b = [],[]
c = str()
n = int(input())
for i in range(n):
    s = input()
    a.append(s)
for i1 in range(len(a)):
    for i2 in range(i1,len(a)):
        if a[i1].isalpha() and a[i2].isalpha():
            if a[i1] == a[i2] and i1!=i2:
                if find1(b,a[i1]):
                    b.append(a[i1])

for i in b:
    c += i
print(c)                    #找出一段字符中多次出现的字母
                            #'hello world!'  --->'lo',且不重复'''
for i in range(len(a)):
    if i>150:
        print(i)
