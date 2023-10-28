'''a= [1,2,3]
f =0 
for i in a:
    f+=i
print(f)

for i in range(26):
    print(chr(65+i))'''
'''def sum(*a):
    f = 0
    for i in a:
        f+=i
    print(f)
sum(1,2,3,4,5,6,7,8,9,10)

sum(112,12)'''

'''a = 6
b = 8
tem = a
a = b
b = tem
print(a)
print(b)

'''

'''a = 10
b =20
a =a+b
b = a-b
print(b)
a = a - b
print(a)'''

'''a = 3
b = 5
print(a|b)'''

'''a = 2
b = 3

a = a ^ b
b = a ^ b
a = a ^ b
print(a)
print(b)'''

'''a = 2
b = 3
a = b
b = a
print(a)
print(b)'''

'''for i in range(10):
    print(i)
else:
    print('akahs')

'''
#if 2 < 5 : print('this is single line code'); print('this is if statement')
'''a = 4
b = 5
max = a if b < a else b
print(max)

min = a if b > a else b
print(min)'''
'''a = [3,5,100,2,6,8,7,9,10,15,20,11,13,12]
f = 0
for i in a:
    if f < i:
        f = i
    elif f == i:
        f == i
    elif f > i:
        f = f
print(f)'''

'''a = {1,2,3,4,5}
b = {4,5,6,7}
for i in b:
    if i in a:
        print(i)'''

'''from array import *
a = array('i',[1,2,3,4,5])
b = 0
for i in a:
    if i == 3:
        print(b)
    b+=1
print(a.index(3))'''

'''a = [12,3,10,4,2,8,6]
n = len(a)
for i in range(n):
    for j in range(i+1,n):
        if a[i] > a[j] :
            tech = a[i]
            a[i] = a[j]
            a[j] = tech
        else:
            pass
print(a)'''

'''a = [12,10,3,10,4,2,8,6]
n = len(a)
for i in range(n):
    for j in range(i+1,n):
        if a[i] == a[j] :
            print(a[i])
        else:
            pass

'''

'''a = [1,2,2,2,3,4]
n = len(a)
a.sort()
for i in range(1,n):
    if a[i-1] == a[i] :
        print(a[i])
'''

#this code is not understand
'''def show(n):
    if n <= 1:
        return n
    else:
        res = show(n-1)
        print(res)
        return res+n
print(show(100))'''


#fabonacci numbers program.
'''i = 0
f = 1
while i < 30:
    print(i)
    f = f + i
    print(f)
    i += f
'''
'''a = [1,2,3,4,1]
print(1 in a)
'''

'''def show(func):
    def method():
        print('first')
        func()
        print('last')
    return method

@show
def fistfunc():
    print('Alax')

fistfunc()'''

'''class Show:
    def __init__(self):
        self.add = 0
        print('my name',self.add)
    def like(self):
        self.add += 1
        print(self.add)
ta = Show()
ta.like()
ta.like()
ta.like()'''

'''def show(num):
    a,b = 0,1
    while a <=num:
        print(a)
        a,b = b,a+b
        print('second A = ',a)
        print('second B =',b)
ca = show(30)
'''

'''a = 'my name is akash'
x=a.replace('name','mian')
print(x)
print(x+a)'''

'''a= [1,2]
if 1 in a:
    print(True)
else:
    print(False)'''

'''a = [1,2,3,4]
print(id(a))
b = [5,6,7,8]
print(id(b))

a.extend(b)
print(a)
print(id(a))
'''

'''def reverselist(lst):
    if not lst:
        return []
    return [lst[-1]] + reverselist(lst[:-1])

print(reverselist([1,2,3,4,5]))


a = [1,2,3,4,5]
print(a[:-1])

'''

def sum(*nums):
    print(nums)
    print(type(nums))
sum(100,200,300,400,1000)