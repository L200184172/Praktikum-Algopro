## activity 1 . perulangan . by : @hafshahfitri
R = {'segitiga' : ' L = 0.5 * a * t' ,
     'persegi' : ' L = s ** 2' ,
     'persegi panjang' : ' L = p * l' ,
     'lingkaran' : ' L = phi * r **2' ,
     'jajaran genjang' : ' L = a * t'}

print (''' 


No  |    Nama Bangun   |   Rumus Luas
----|------------------|---------------
1   | segitiga         | %s
2   | persegi          | %s
3   | persegi panjang  | %s
4   | lingkaran        | %s
5   | jajaran genjang  | %s

'''%(R['segitiga'], R['persegi'], R['persegi panjang'], R['lingkaran'], R['jajaran genjang']))
print ('---------------------------------------------------')

## activity 2 . password . by : @hafshahfitri
n = 0
while n<3:
    x = input ('insert password : ')
    n +=1
    if x=='hafshah':
        print ('congratulation! you can log in!')
        n=3
    if x!='hafshah':
        if n==3 :
            print ('sorry, you have try 3 times. you can not log in')
        elif x!='hafshah' :
            print ('sorry, your password was wrong')
print ('---------------------------------------------------')

## activity 3 . ucapan selamat . by : @hafshahfitri
h = ('morning' , 'noon' , 'afternoon' , 'evening' , 'night')
d = input ('enter your name : ')
v = input('what time is it now? ')
v = float (v)
if v>=01.00 and v<=10.00:
    print ('good' , h[0] , d)
elif v>=10.01 and v<=14.59:
    print ('good' , h[1] , d)
elif v>=15.00 and v<=18.00:
    print ('good' , h[2] , d)
elif v>=18.01 and v<=20.59:
      print ('good' , h[3] , d)
elif v>=21.00 and v<=24.59:
    print ('good' , h[4] , d)

print ('---------------------------------------------------')





    
             
             
