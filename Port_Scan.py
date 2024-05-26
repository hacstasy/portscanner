from socket import *

if __name__ == '__main__':
   target = input('Target: ')
   localip = gethostbyname(target)
   print ('Starting scan on host: ', localip)
   
   for i in range(50, 500):
      s = socket(AF_INET, SOCK_STREAM)
      
      conn = s.connect_ex((localip, i))
      if(conn == 0) :
         print ('Port %d: OPEN' % (i,))
      s.close()
