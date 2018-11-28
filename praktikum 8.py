##Activity 1 . modul . by : @hafshahfitri
print ('''
Activity 1
''')
CV = {'Name' : 'Hafshah Fitri Afifah',
      'NIM' : 'L200184172',
      'Address' : 'Griya Bumi Makmur 2 no. 1',
      'City' : 'Kendal',
      'Province' : 'Jawa Tengah',
      'PostCode' : '51314',
      'Majors' : 'Informatics Engineering',
      'Faculty' : 'FKI'}

def Name():
    print (CV['Name'])
def NIM():
    print(CV['NIM'])
def Address():
    print(CV['Address'])
def City():
    print (CV['City'])
def Province():
    print(CV['Province'])
def PostCode():
    print(CV['PostCode'])
def Majors():
    print(CV['Majors'])
def Faculty():
    print(CV['Faculty'])
              

def OptionAvailable():
    print ('''Option Available :
b showing
1 showing NIM
2 showing Name
3 showing Address
4 showing City
5 showing Province
6 sjowing Post Code
7 showing Majors
8 showing Faculty
c close the program
''')
    
OptionAvailable()

while True:
    x = input ('Your Choice: ')
    if x == 'b':
        OptionAvailable()
    elif x == '1':
        NIM()
    elif x == '2':
        Name()
    elif x == '3':
        Address()
    elif x == '4':
        City()
    elif x == '5':
        Province()
    elif x == '6':
        PostCode()
    elif x == '7':
        Majors()
    elif x == '8':
        Faculty()
    elif x == 'c':
        print ('Thank You')
        break
    else:
        print ('Invalid Choice')
        

##Activity 2 . function
print ('''
 Activity 2
''')
def conversionTemperature(C=0, F=0):
    if C != 0:
        F = int(9 / 5 * C + 32)
        print ('Temperature', C , 'Celcius equivalent to', F , 'Fahrenheit')
    elif F != 0:
        C = int(5 / 9 * (F - 32))
        print ('Temperature', F , 'Fahrenheit equivalent to' , C , 'Celcius')
    elif F != 0 and C != 0:
        F = int (9 / 5 * C + 32)
        print ('Temperature', C , 'Celcius equivalent to', F , 'Fahrenheit')
    else :
        F = int(9 / 5 * C + 32)
        print ('Temperature', C , 'Celcius equivalent to', F , 'Fahrenheit')

## 
    
        
