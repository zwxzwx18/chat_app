import socket
import sys
from threading import Timer
import time


HOST = ''   
PORT = 9000 
 

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
print 'Socket created'
 
try:
    s.bind((HOST, PORT))
except socket.error , msg:
    print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()
     
print 'Socket bind complete'
 
s.listen(10)
print 'Socket now listening'

user={} #{user, addr}
flag={} #{user, flag}
ac={} #{user, conn}
dict={} #{user, content}
content=[] #contain the messages

a='12345'
print a[0:2]
#while 1:

#   print 'a'
    
    #   for i in user
    #   if flag[i]!=0
    #       k=dict[i][0]
    #       conn=ac[i]
    #       while dict[i][k]
    #           conn.send(dict[i][k])
    #           time.sleep(0.5)
    #           k=k+1
    #       dict[i][0]=k
    #       flag[i]=0

conn, addr = s.accept()

#   flag=1
print 'Connected with ' + addr[0] + ':' + str(addr[1])
#   print conn
#   reply = 'OK...'
#   conn.send(reply)

#   data=conn.recv(1024)
#   if not data:
#       print 'OK...'
#   else:
#       print data

time.sleep(1)

conn.close()
s.close()
