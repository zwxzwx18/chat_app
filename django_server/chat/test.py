import socket
import sys
from threading import Timer
import time
import threading
from chatdata.models import User, content

#from chatdata.models import User, content


class receive(threading.Thread):
    def run(self):
        i=1
        global s
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
        
        global user
        user={} #{user, addr}
        global flag #{user, flag}
        flag={}
        global ac
        ac={} #{user, conn}
        global dict
        dict={} #{user, content}
        global content
        content=[] #contain the messages
        while i<3:
            i=i+1
            print 'a'
            conn, addr = s.accept()
            print 'Connected with ' + addr[0] + ':' + str(addr[1])
            
            data=conn.recv(1024)
            print data
            print 'b'
            k=0
            while data[k]!=':' :
                k=k+1
            print data[0:k]
            u=data[0:k]
            try:
                User.objects.get(user=u)
            except:
                p=User(user=u, addr=addr, conn=conn, flag=1, index=1, length=1)
                p.save()
                #p.content_set.create(message=1)
                p.content_set.create(message=data[k+1:-1], index=1)
            else:
                p=User.objects.get(user=u)
                p.addr=addr
                p.conn=conn
                p.flag=1
                #p.index=p.index+1
                p.length=p.length+1
                p.content_set.create(message=data[k+1:-1], index=p.length)

#p=User(user="a", addr="100.1", conn="100.2", flag=1, index=1)
#p.save()
class send(threading.Thread):
    def run(self):
        j=0
        while j<7:
            
            print 'b'
            j=j+1
            #userlist=list(User.objects.all())
            for p in User.objects.all():
                if p.flag!=0:
                    print 'fuck'
                    k=p.index
                    conn=p.conn
                        if k<=p.length:
                        while 1:
                            #print dict[i][k]
                            conn.send(content.objects.get(user=p, index=k))
                            time.sleep(1)
                            k=k+1
                            if k>p.length:
                                break
                        p.index=k
                        p.flag=0
            time.sleep(5)


for user in User.objects.user
    print user
r=receive()
t=send()
r.start()
time.sleep(3)
t.start()

#p=User(user="a", addr="100.1", conn="100.2", flag=1, index=1)
#p.save()