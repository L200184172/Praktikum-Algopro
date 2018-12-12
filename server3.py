#nama berkas: p_tcpser.py
#TCP Server untuk client p_tcpcli.py

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("",50004))
s.listen(5)
print "calculate the area of rectangle"
data = ''
while data.lower() != 'quit' :
       komm, addr = s.accept()
       side = 0
       while data.lower() != 'quit':
              data = komm.recv(1024)
              if data.lower() == 'quit' :
                     s.close()
                     break
              print'Command: ', data
              try:
                     side = int(data)
                     komm.send('stored data')
              except ValueError:       
                     if data.lower() == 'calculate':
                            respon = 'the area of rectangle with a side '+str(side)+' = '+str(side*side)
                            komm.send(respon)
              
                     else:
                            komm.send('unknown command') 
