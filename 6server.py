import socket
import sys
import time
import errno
import math        
from multiprocessing import Process

ok_message = '\nHTTP/1.0 200 OK\n\n'
nok_message = '\nHTTP/1.0 404 NotFound\n\n'

def process_start(s_sock):
    s_sock.send(str.encode('mini calculator'))
    while True :
        data = s_sock.recv(2048)                     
        data = data.decode("utf-8")

        #calculation process
        try:
            operation, value = data.split()
            operate = str(operation)
            num = int(value)

            if operate == 'log':
                ans = math.log10(num)

            elif operate == 'squareroot':
                ans = math.sqrt(num)

            elif operate == 'exponent':
                ans = math.exp(num)

            elif operate == 'exit':
                ans = ('process has ended')  

            else:
                ans = ('ERROR')

            result = (str(operate) + ' ' + str(num) + ' = ' + str(ans))
            print ('result: ' + str(ans) )
        except:
            print ('error')
            result = ('error')
            

        

        if not data:
            break

        s_sock.send(str.encode(result))
        #s_sock.sendall(str.encode(ok_message))
    s_sock.close()

if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("",8828))
    print("listening for the response")
    s.listen(10)

    try:
        while True:
            try:
                s_sock, s_addr = s.accept()
                p = Process(target=process_start, args=(s_sock,))
                p.start()

            except socket.error:

                print('got a socket error')

            except Exception as e:
                print("an exception occurred!")
                print(e)
                sys.exit(1)
    finally:
           s.close()
