#nama berkas: p_tcpser.py
#TCP Server untuk client p_tcpcli.py

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("",50001))
s.listen(5)
print "Automatic answering machine is ready"
data = ''
dictionary = {'name' : 'Hafshah Fitri Afifah',
          'NIM' : 'L200184172',
          'generation' : '2018'}
while data.lower() != 'exit' :
       komm, addr = s.accept()
       while data.lower() != 'exit':
              data = komm.recv(1024)
              if data.lower() == 'exit' :
                     komm.send('ready!!')
                     s.close()
                     break
              print'Question: ', data
              if dictionary.has_key(data):
                     komm.send(dictionary[data])
              else:
                     komm.send('Your question is irrelevant')
