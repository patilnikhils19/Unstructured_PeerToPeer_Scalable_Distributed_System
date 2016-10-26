import os
import argparse
import sys
import socket
import socket
import subprocess
import time
import thread
from thread import *
import datetime
import logging


class Table(object):
    def __init__(self):
        self.rows =  []
        self.IPA = {} # look for the IP Adress

    def addRow(self, row):
        self.rows.append(row)
        self.IPA[row['IP']] = row

    def getrowbyindex(self, Index):
        return self.rows[Index]
    def getIp(self, Index):
        d = self.rows[Index]
        ip = d.get('IP')
        return ip

    def getPort(self, Index):
        d = self.rows[Index]
        port = d.get('Port')
        return port

    def getResource(self, Index):
        d = self.rows[Index]
        resource = d.get('Resource')
        return resource

    def getLen(self):
        l = len(self.rows)
        return l
    
    def getTable(self):
        m = self.rows
        return m

    def getTS(self, Index):
        d = self.rows[Index]
        t = d.get('TS')
        return t

    def delTable(self):
        d = self.rows
        del d[:]
        self.rows = d

    def getRemove(self, IP ,Port):
        l = len(self.rows)
        i = 0
        while (i<l):
            d = self.rows[i]
            ip = d.get('IP')
            ip = str(ip)
            port = d.get('Port')
            port = int(port)
            if (IP == ip and port == Port):
               j = i
            i = i+1
        del self.rows[j]
        return j

    def updateIndex(self, j):
        l = len(self.rows)
        while (j<l):
            d = self.rows[j]
            ip = d.get('IP')
            port = d.get('Port')
            index = d.get('Index')
            index = int(index)
            index = index -1
            del self.rows[j]
            row = {'Index': index,'IP': ip, 'Port': port}
            self.rows.insert(j,row)
            j = j+1




def genquery():
    N = 160
    s = raw_input("s>>")
    s =float(s)
    Ns = raw_input("Ns>>")
    Ns = int(Ns)
    n = int(1)
    k = int(1)
    p = 0.0
    b = []
    while (k <= 160):
          a = 0.0
          a = (1/pow(k,s))
          while(n<=N):
                p = p +(1/pow(n,s))
                n = n +1
          b.append((a/p))
          k = k+1
    logging.info('This message should go to the log file')
    j = 0
    print sum(b)
    while (j<len(b)):
          b[j] =round(b[j]*Ns)
          if (b[j] == 0):
             b[j] = 1
          j = j+1
   # print b
   # print sum(b)
    logging.info('the data is as next\t'+ str(b))
    f = open('Resources.txt','w')
    with open("resourcesq.txt", "r") as source:
         array = []
         for line in source:
             array.append(line)
         x = 0
         while (x<len(b)):
               i = 0
               while (i<b[x]):
                     f.write(array[x])
                     i = i + 1
               x = x+1
    f.close()


def join(number):

    logging.info('Joining with the nodes')
    NodeIp = table.getIp(number-1)
    NodePort = table.getPort(number-1)
    NodePort = int(NodePort)
    Node = (NodeIp,NodePort)
    protocol = "JOIN"
    List = [protocol,host1,port1]
    List = ' '.join(map(str, List))
    a = len(List)+5
    c = "{0:0=4d}".format(a)
    List1 = [c,protocol,host1,port1]
    List1 = ' '.join(map(str, List1))
    List1 = str(List1)
    logging.info('Joining with the node')
    logging.info(str(List1))
    print List1
    print ("Joining with the Node\n" + str(NodeIp))
    sock.sendto(List1, Node)#Send Request to Node
    print "Joining Request send"
   # data, address = sock.recvfrom(1024)#Recieve data from Node
   # logging.info('Recieved response from the node for joining')
   # logging.info(str(data))
    #print "The response from the Node\n" + str(data)


def Register():

    
    if not args.username :
       username = raw_input("Please Give Username for registering with the Bootstrap Server:> ") #Get username from the server
    else :
       username = args.username

    """Formation of the string according to given protocol for the bootstrap server"""

    protocol = "REG"
    List = [protocol,host1,port1,username]
    List = ' '.join(map(str, List))
    a = len(List)+5
    c = "{0:0=4d}".format(a)
    List1 = [c,protocol,host1,port1,username]
    List1 = ' '.join(map(str, List1))
    List1 = str(List1)
    logging.info('Sending Protocol Message For Regestration to Bootstrap')
    logging.info(List1)
   # print List1
   # print type(List1)
   # print server
    print ("registering with the Bootstrap Server\n")

    sock.sendto(List1, (server))#Send Request to server
	
    data, address = sock.recvfrom(1024)#Recieve data from server

    print "The response from the Bootstrap\n" + str(data)

    logging.info('Recieved Protocol Message From Bootstrap')
    logging.info(str(data))

    if (data.find("REGOK") != -1) :
       print "Registration Successful with the Bootstrap Server\n"
       logging.info('Registration Successsful')
       connection = data.split()

       i = int(connection[3])
      
       if (i != 0 and i < 100) :
         # table = Table()
          number = 1
          z = 3
          y = 4
          while (number <= i):
             # print number
              table.addRow({'Index': number,'IP': connection[z+number], 'Port': connection[y+number]})
              z = z+1
              y = y+1
              row = table.getrowbyindex(number-1)
              logging.info('Registred  IP Recieved From The Bootstrap')
              logging.info(row)
             # print row
              join(number)
              number = number +1
    else :
       print "Regisration with Bootstrap Server is unsuccessful, Please try again!\n"
       logging.info('Registration failed with the bootstrap')



def clientserver():
               #print routing table
               # m = table.getTable()
               # print m
               while True: 
                       string = raw_input(">>")
                       print string
                       if (string == 'genquery()'):
                          genquery()
                          with open("Resources.txt", "r") as source:
                               arr = []
                               for line in source:
                                   arr.append(line)
                          s = 0
                          global flag
                          while True:
                            if (s<len(arr)):
                              # if (flag == 0):
                            	  string = arr[s]
                                  print "Query is:"
                                  print string
                            	  resource = string
                             	  search(resource,host1,port1)
                             	  s= s+1
                                  time.sleep(1)
                                  flag = 1
                            else:
                                  logging.info('Lattencies are')
                                  logging.info(LAT)
                                  logging.info('Hop counts are')
                                  logging.info(HOP)
                                  logging.info('Delay time is')
                                  logging.info(DELE)

                                  f = open('Lat.txt','w')
                                  x = 0
                                  while (x<len(LAT)):
                                        f.write(str(LAT[x]))
                                        x = x+1
                                  f.close()
                      		 

                                  break
                   

                       elif (string != 'exit()' and string != 'genquery()'):  
                          resource = string
                          search(resource,host1,port1)
                                                               
                       elif (string == 'exit()'):
                           logging.info('exit() request recieved')
                           length = table.getLen()
                         # print length
                           j = 1
                           while (j <= length):
                                      NodeIp = table.getIp(j-1)
                                      NodePort = table.getPort(j-1)
                                      NodePort = int(NodePort)
                                      Node = (NodeIp,NodePort)
                                      protocol = "LEAVE"
                                      List = [protocol,host1,port1]
                                      List = ' '.join(map(str, List))
                                      a = len(List)+5
                                      c = "{0:0=4d}".format(a)
                                      List1 = [c,protocol,host1,port1]
                                      List1 = ' '.join(map(str, List1))
                                      List1 = str(List1)
                                      sock.sendto(List1, Node)#Send Leave Request to Node
                                      logging.info('Leave request send to Routing table node' + List1)
                                      j = j + 1
                

def thread(sock):

                while True:
                     # print "ready to accept data"
                      logging.info('Thread is accepting request')
                      data1, address = sock.recvfrom(1024)
                      logging.info('New request recieved')
                      logging.info(data1)
                     # print "data"+ data1
                      if data1 :
                         t1 = time.time()
                        # print data1
                         if (data1.find("JOIN") != -1 and data1.find("OK")== -1):
                            data1 = data1.split()
                            ip = data1[2]
                            logging.info('IP requested  to join')
                            logging.info(ip)
                            print "ip requested to join" + ip
                            port = data1[3]
                            port = int(port)
                            addr = (ip,port)
                            number = table.getLen() +1
                         #  print number
                            table.addRow({'Index': number,'IP': ip, 'Port': port})
                            row = table.getrowbyindex(number-1)
                            logging.info('New IP joining added to the routing table')
                            logging.info(row)
                        #    print "row added" 
                        #    print row
                            protocol = "JOINOK"
                            List = [protocol,0]
                            List = ' '.join(map(str, List))
                            a = len(List)+5
                            c = "{0:0=4d}".format(a)
                            List1 = [c,protocol,0]
                            List1 = ' '.join(map(str, List1))
                            out  = str(List1)
                            sock.sendto(out, addr)
                            logging.info(out)
                            logging.info('Response send for the join')
                        #    print ("join response send")
                            t2 = time.time()
                            Delay_Join = t2-t1
                            logging.info('Delay time for serving join request\t' + str(Delay_Join))

if __name__ == '__main__':

          parser = argparse.ArgumentParser()#Define argument parser
          parser.add_argument("-p","--port",help="Port Number",type=int)
          parser.add_argument("-b","--bootstrapip",help="Bootstrap Server IP address",type=str)
          parser.add_argument("-n","--bootstrapport",help="Bootstrap Server Port Number",type=int)
          parser.add_argument("-u","--username",help = "Username for registering with the bootstrap Server",type=str)
          args = parser.parse_args()

          if not args.bootstrapip or  not args.port or not args.bootstrapport :
                 print("Need Bootstrap ServerIP")

          elif not args.port :
                 print("Need Port Number")

          elif  not args.bootstrapport :
                 print("Need Bootstrap Server Port Number")

          else :
                port1 = args.port
                host = args.bootstrapip #Get Bootstrap IP from arguments
                sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)#create socket
                h = socket.gethostname() #Get host name
                host1 = socket.gethostbyname(h) #Get Host IP address
                self = (host1,port1)
                server = (host,args.bootstrapport)
                try:
                        sock.bind((host1, port1))
                        print 'bind complete'
                except socket.error , msg:
                        print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
                        sys.exit()

		table = Table()
                table1 = Table()
                LAT = []
                HOP = []
                DELE = []
                flag = 0
                T1 = 0.0
                T2 = 0.0
                logging.basicConfig(filename='log.log',filemode='a',format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',datefmt='%m/%d/%Y %I:%M:%S %P',level=logging.DEBUG)
                with open("log.log", "w") as file:
                     file.truncate()
                logging.info('The Node has started')
		Register()
		start_new_thread(thread,(sock,)) #Create new threads for connecting clients
		clientserver()



