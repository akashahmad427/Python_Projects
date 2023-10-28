from time import *
import random as r



def mistake(partest,usertest):
    error = 0
    for i in range(len(partest)):
        try:
            if partest[i] != usertest[i]:
                error = error + 1
        except:
            error = error + 1
    return error

def speed_time(time_start,time_end,userinput):
    time_delay = time_end -time_start
    time_round = round(time_delay,2)
    speed = len(userinput) / time_round
    return round(speed)

while True:
    ck = input('ready to test : yes / no : ')
    if ck == 'yes':
                
                test = ['Hi my name is akash',
                        'I live in village of 427',
                        'my father name is ishtiaq ahmad ',
                        'he is a farmer']
                test1 = r.choice(test)
                print('*********typing speed calculator')
                print(test1)
                print()
                time_1=time()
                testInput = input('Enter : ')
                time_2 = time()

                print('Speed : ',speed_time(time_1,time_2,testInput),'w/sec')

                print('Error : ',mistake(test1,testInput))
    elif ck == 'no':
        print('thank you')
        break
    else:
        print('Wrong input...')
         
