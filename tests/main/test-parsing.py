
class _host:
    def __init__(self,hostname):
        self.hostname=hostname
        self.online=False

# Host file parsing
def host_parse(hostfile):
    lines=hostfile.read().split("\n")
    lines=lines[:len(lines)-1] # cleans excess ''
    hosts=[]
    
    #Create host objects from config files
    for host in lines:
        hostname=host.split(",")[0]
        hosts.append(_host(hostname))
    # Then below interact with objects

    # And return all hosts
    return hosts

print(host_parse(open("hosts","r")))
