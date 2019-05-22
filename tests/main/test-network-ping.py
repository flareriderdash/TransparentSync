import subprocess

class _host:
    def __init__(self,hostname):
        self.hostname=hostname
        self.online=False

# Tests for connectivity 
def ping(host):
    cmd={
            "ping" : ["ping", "-c 4" , host.hostname]
        }
    try:
        subprocess.check_output(cmd["ping"])
        host.online=True
        return True
    except:
        host.online=False
        return False



# create list of host objects
hosts=[_host("Flare-121"), _host("Flare-120")]


for Object in hosts:
    ping(Object)
