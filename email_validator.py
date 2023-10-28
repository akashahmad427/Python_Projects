a = input('enter your email = ')
d,e,f = 0,0,0
if len(a) >= 6:
    if a[0].isalpha():
        if ('@' in a) and (1 == a.count('@')):
            if (a[-4] == '.') ^ (a[-3] == '.'):
                for i in a:
                    if i == i.isspace():
                        d = 1
                    elif i.isalpha():
                        if i == i.upper():
                            e = 1
                    elif i.isdigit():
                        continue
                    elif i=='_' or i=='.' or i=='@':
                        continue
                    else:
                        f = 1
                if d == 1 or f == 1 or e == 1:
                    print('wrong email 5')
                else:
                    print('correct email')
            else:
                print('wrong email 4')
        else:
            print('wrong email 3')
    else:
        print('wrong email 2')
else:
    print('wrong email 1')