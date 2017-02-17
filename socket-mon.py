#CMPE-273-Lab#1 : socket monitoring tool
import psutil

class Procid:
    __slots__='pid','laddr','raddr','status'

    def __init__(self,pid,laddr,raddr,status):
        self.pid =pid;
        self.laddr =laddr;
        self.raddr =raddr;
        self.status =status

    def __repr__(self):
            return "%s %s %s %s " % ('"'+ str(self.pid)+'"'+"," , '"'+str(self.laddr)+'"'+","  , '"'+str(self.raddr)+'"'+","  ,'"'+str(self.status)+'"')

def start():

    list1=[] #get list of all pid
    list2=[] #get list of (pid,laddr,raddr,status)

    for i in psutil.net_connections(kind='tcp'):
            list1.append(i.pid)
            list2.append(Procid(i.pid,i.laddr,i.raddr,i.status))

    pidcounter = dict() #get the number of connectionss per pid
    for j in list1:
        pidcounter.setdefault(j,0)
        pidcounter[j] +=1

    final=sorted(pidcounter,key=lambda X:pidcounter[X]) #get sorted list of pid based on count
    final.reverse() #get the list in descending order

    for k in list2:
        if k.laddr:
            k.laddr="%s@%s" % k.laddr

    for z in list2:
        if z.raddr:
            z.raddr="%s@%s" % z.raddr

    print '"pid","laddr","raddr","status"'

    for x in final:
        for y in list2:
           if x==y.pid:
               print y

if __name__ == '__main__':
    start()
