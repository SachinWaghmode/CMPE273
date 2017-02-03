import subprocess

class Host:
    __slots__ = 'ip','region','avg'

    def __init__(self,region,ip):
	self.region =region;
	self.ip =ip;
	self.avg=0


    def __str__(self):
        return 'Ip:',self.ip,' AVG:',self.avg

    def __repr__(self):
        return 'Ip:'+self.ip+' AVG:'+str(self.avg)

def start():
    	
	count=1
	HostList = []
    	HostList.append(Host("us-east-1","54.86.63.252"))            
    	HostList.append(Host("us-west-1","54.219.127.255"))
    	HostList.append(Host("eu-west-1","54.72.255.252"))
	HostList.append(Host("us-west-2","52.13.255.255"))
	HostList.append(Host("eu-central-1","52.29.63.252"))
	HostList.append(Host("us-gov-west-1","52.222.9.163"))
	HostList.append(Host("eu-west-2","52.56.34.0"))
	HostList.append(Host("ca-central-1","52.60.50.0"))
	HostList.append(Host("us-east-2","52.15.55.0"))
	HostList.append(Host("ap-northeast-1","54.64.0.2"))
	HostList.append(Host("ap-northeast-2","52.79.52.64"))
	HostList.append(Host("ap-southeast-1","52.76.191.252"))
	HostList.append(Host("ap-southeast-2","54.66.0.2"))
	HostList.append(Host("ap-south-1","52.66.66.2"))
	HostList.append(Host("sa-east-1","54.233.127.252"))

    	for item in HostList:
        
		ping = subprocess.Popen(
            	["ping", "-c", "3", item.ip],
            	stdout = subprocess.PIPE,
            	stderr = subprocess.PIPE
    		)

       	 	out, error = ping.communicate()
        
       		b=out.split('stddev')

		c=b[1].split("/")
		
       	 	item.avg= float(c[1])
        	
      	HostList.sort(key=lambda Host: Host.avg)
       		
        for h in HostList:
            print count,'.','',h.region,' \t ','[',h.ip,']',' - ', h.avg
            count=count+1


if __name__ == '__main__':
    start()