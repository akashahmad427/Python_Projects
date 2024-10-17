lstside=['north','east','west','south','south','north']



'''a = []
n = len(lstside)
for i in lstside:
    for j in range(n):
        if i == lstside[j]:
            if lstside.index(i)  == j :
                continue
            else:
                print(i)
                if i not in a:
                    a.append(i)
print(a)'''
'''from functools import *
a = [1,2,3,7,4,5]
n = len(a)
i = 0
while i < n:'''

'''def fun(a):
    n=len(a)
    tech=a[0]
    a[0] = a[n-1]
    a[n-1] = tech 
    print(a)
a = [200,2,3,4,10]
fun(a)'''

'''from turtle import *
for i in range(1,100,3):
    circle(i)'''
'''for i in range(1,10,2):
    for j in range(-4,0):
        print(' '*(-j),end='')
        print(i*'*')
'''
'''n = 10
for i in range(1,10,2):
    m=int((n-i-1)/2)
    print(' '*m,end='')
    print('*'*i)
 '''
'''for i in range(-10,-1):
    print('*'*(-i),end='')
    print('  '*((i)+10),'*'*(-i))
'''
'''for i in range(1,101):
    if i%2==0:
        print(i,end=' ')
'''
        
'''i = 0
while True:
    print(i)
    if i == 3:
        break
    i +=1'''

'''for i in range(5):
    for j in range(1,5):
        print(j)
        if j == 3:
            break
    print(i)'''
'''a = [1,2,3,4,5]
if 1 in a:
    print(True)'''

'''a = [3,5,2,8,1,9,10,2,5,7,12,3,0,6]
a.sort()
n = len(a)
print('maximum number is = ',a[n-1])'''
'''a = [1,2,3]
b = []
for i in a:
    c=i*i
    b.append(c)
print(b)'''

'''for i in range(1,5):
    print()
    for j in range(i):
        print(j+i,end='')
    
'''

'''a = [1,2,3,4,5]
a.append(6)
print(a)

a.insert(0,7)
print(a)

a.pop(2)

print(a)
n = int(input('enter a number of element = '))
a =[]
for i in range(n):
    a.append(int(input('enter an elemet = ')))
print(a)'''

'''a = [1,2,3,4,5,6,7]
even = 0
odd = 0

for i in a:
    if i%2==0:
        even = even+i
    else:
        odd = odd+i


print('sum of even numbers = ', even)
print('sum of odd number = ',odd)'''

'''a = [1,2,3,4,5,4,6,3,4,5,6,7,8,3,90,5,67,45,3,4,5,2,67,89,90,100]
n = len(a)
#c= n-1
end = int(input('enter a number = '))
print(a[n-end:])

'''
'''a = [[1,2,3],
     [4,5,6],
     [7,8,9]]
print(a[0:2][0])'''

'''class First():
    def __init__(self,n,m):
        self.name = n
        self.roll = m
information=First('akash',123)
print(information.name)
print(information.roll)'''

'''x=0
for row in range(5):
    for col in range(row):
        x=x+1
        print(x,end='')
    print()'''
'''for i in range(1,5):
    print()
    for j in range(i):
        print(i+j,end='')'''

'''a = {'name':'akash','roll':123}
del a['roll']
print(a)'''

'''a = {'name':'akash','roll':123}

for value in a.values():
    print(value)'''

'''class First():
    def __init__(self,name,roll):
        self.name = name
        self.roll = roll
    def show(self):
        print('first function')
    
    def method(self):
        print('this is method function')
class Second(First):
    def get(self):
        print('this is second class get function')
    
    def set(self):
        print('this is second class set function')

f = Second('akash',123)
print(f.name)
print(f.roll)
f.show()
f.method()
f.get()'''

'''class A:
    def first(self):
        print('this is first class function.')

class B(A):
    def second(self):
        print('this is second class function.')

h = B()
h.first()
h.second()'''

'''class Employee():
    totalemployee = 0

    def __init__(self,name):
        self.name = name
        Employee.totalemployee +=1

emp1 = Employee('akash')
print(Employee.totalemployee)
'''

'''class First():
    def __init__(self):
        print('this is first function ')
    
    def __del__(self):
        print('this is delete function')
a = First()
print('***************')
del a'''

'''class First:
    def __init__(self,name,roll):
        self.name = name
        self.roll = roll

    def getName(self):
        return self.name

    def setName(self,name):
        self.name = name
c = First('akash',123)
print(c.getName())
c.setName('hassan')
print(c.getName())'''

'''class First:
    name = 'cat'
    _color = 'brown'
    __age = 22

a = First()
print(a.name)
print(a._color)
print(a._First__age)
'''
'''class First:
    def __init__(self):
        self.name = 'Python'
        self.ifun = self.Innerfunction()
    def show(self):
        print('language name = ',self.name)

    class Innerfunction():
        def method(self):
            print('this is introduce in 1990')


te = First()
print(te.name)
te.show()
iner = te.Innerfunction()
iner.method()'''

'''class Grandfather:
    def thow(self):
        print('this is grand father class ')


class Father(Grandfather):
    def show(self):
        print('this is father class ')

class Son(Father):
    def method(self):
        print('this is son class function')
    
s = Son()
s.show()
s.thow()
s.method()'''

'''class First:
    def __init__(self):
        print('self',id(self))

obj = First()
print('object id = ',id(obj))'''

'''class Track:
    def model(self):
        print('model = 2020')

    def color(self):
        print('the color of truck is red')

class Car:
    def model(self):
        print('model = 2023')

    def color(self):
        print('the color of car is black')

def fun(obj):
    obj.model()
    obj.color()
tr = Track()
ca = Car()
for i in (tr,ca):
    tr.model()
    tr.color()
    print('&&&&&&&&&&&&&&')'''

'''class Function:
    def type(self):
        print('we have different vehicals')

class Car(Function):
    def speed(self):
        print('the speed of car is faster...')

class Truck(Function):
    def speed(self):
        print('the speed of truck is slower...')

fun = Function()
fun.type()
print('___________________')
ca = Car()
ca.type()
ca.speed()
print('___________________________')
tar = Truck()
tar.type()
tar.speed()'''

'''class Duck:
    def walk(self):
        print('thapk thapk thapk')

class Crow:
    def walk(self):
        print('caw caw caw caw')

class Cat:
    def talk(self):
        print('meao meao meao')


def fun(obj):
    if hasattr(obj,'walk'):
        obj.walk()
    if hasattr(obj,'talk'):
        obj.talk()

duck = Duck()
crow = Crow()
cat = Cat()
fun(duck)'''

'''a = ['a',1,2,3,4,'b',4,5,6,'c']
for i in a:
    if type(i) is str:
        print(i)
    '''
'''try:
    age = int(input('enter your age'))
    if age<=18:
        raise AgeError
except Exception as e:
    print('something went wrong... = ',e)

else:
    print('allowed')'''
'''tup = (1,2,3,4)
dic = {tup:1}
print(dic)

list1 = [1,2,3,4]
dic = {list1:1}
print(dic)'''

'''a = {1,2,3,4,5}
b = {5,6,7,8,9}
c=b.issubset(a)
print(c)

a = {1,2,3,4,5,6,7}
b = {3,4,5}

c = a.issubset(b)
print(c)'''

#a = open('text.py','w')

a = 'akash'
for i in a:
    if i == 'k':
        break
    print(i)
