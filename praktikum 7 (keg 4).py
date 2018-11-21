## activity 4 . by : @hafshahfitri

import time
print ('*the program displays computer time*')
a = time.localtime()
c = 2
while c != 0 :
    c = a.tm_sec
    b = time.localtime()
    print (a.tm_hour, ':' , a.tm_min, ':', c)
    while b==a :
        b = time.localtime()
    a=b
print ('practicum time is over')
    
    
