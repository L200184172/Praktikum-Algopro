## activity 1 . write text file . by : @hafshahfitri

file = open('L200184172' , 'w')
file.write( 'L200184172' + '\n')
file.write('18-01-1999' + '\n')
file.write('Hafshah Fitri Afifah' + '\n' )
file.close()


## activity 2 . read text line . by : @hafshahfitri

a = open('L200184172', 'r')
NIM = a.readline()
City = a.readline()
TTL = a.readline()
Name = a.readline()
print (NIM)
print (City + TTL)
print (Name)
a.close()


## activity 3 . read text and save to shelve . by: @hafshahfitri

import shelve
b = shelve.open ('hafshah.data')
b['data'] = [NIM, TTL , Name]
b.close ()

## activity 4 . read shelve . by : @hafshahfitri

import shelve
s = shelve.open('hafshah.data', 'r')
for i in s ['data'] : 
    print (i)
s.close