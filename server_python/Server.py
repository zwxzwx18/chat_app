import socket
import sys
from threading import Timer
import time
import threading
#from chatdata.models import User, content

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
            if user.get(u):
                user[u]=addr
                ac[u]=conn
                flag[u]=1
                content=dict[u]
                #content[0]=content[0]+1
                content.append(data[k+1:-1])
                dict[u]=content
                print dict[u]
            else:
                user[u]=addr
                print user[u]
                ac[u]=conn
                print ac[u]
                flag[u]=1
                content=[]
                content.append(1)
                content.append(data[k+1:-1])
                print content
                dict[u]=content

class send(threading.Thread):
    def run(self):
        j=0
        while j<7:
    
            print 'b'
            j=j+1
            for i in user:
                if flag[i]!=0:
                    print 'fuck'
                    k=dict[i][0]
                    conn=ac[i]
                    if k<len(dict[i]):
                        while 1:
                            print dict[i][k]
                            conn.send(dict[i][k])
                            time.sleep(1)
                            k=k+1
                            if k>=len(dict[i]):
                                break
                        dict[i][0]=k
                        flag[i]=0
            time.sleep(5)


r=receive()
t=send()
r.start()
time.sleep(3)
t.start()
#time.sleep(3)
#conn.close()

#s.close()
