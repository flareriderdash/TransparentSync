#!/usr/bin/python3
import scripts
import subprocess
import datetime

DEBUG=1
FATAL=2

# Host class to turn config host files into actual data structures
class _host:
    def __init__(self,hostname):
        self.hostname=hostname
        self.online=False

# logging, Duh
def log(priority,message):
    if (priority == DEBUG):
        priority = "[DEBUG, %s] " % datetime.datetime.now()
    elif (priority == FATAL):
        priority = "[FATAL, %s] " % datetime.datetime.now()
    logfile.write(priority + message+"\n")
    logfile.flush()

# takes host object and does operations testing network connectivity
def ping(h):
    log(DEBUG, "Pinging host: " +h.hostname)
    cmd={ 
            "ping" : ["ping","-c 2",h.hostname]
        }
    try:
        subprocess.check_output(cmd["ping"])
        h.online=True
        log(DEBUG,"Ping Success!")
        return True
    except:
        h.online=False
        log(DEBUG,"Ping failed!")
        return False

# Parses host files and return _host objects
def host_parse(hostfile):
    log(DEBUG, "Parsing Hosts")
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

# Get all User defined functions from "scripts" dir and execute them
# h is a _host object 
def execute_functions(h):
    global log
    global logfile
    global DEBUG
    global FATAL
    for i in dir(scripts):
        if "__" not in i :

        # Get pointers to functions included in module inbound
         script=getattr(scripts,i)

        # Set logging pointers for scripts plugin
         setattr(script,"logfile",logfile) 
         setattr(script,"log",log) 
         setattr(script,"DEBUG",DEBUG)
         setattr(script,"FATAL",FATAL)
         script.execute(h)

def main():

    identity_file=open("hosts","r")
    log(DEBUG, "Logging initialized")

    hosts=host_parse(identity_file) #returns list of host objects
    
    # For every host execute all anon funcs
    # (Which hosts that functions are executed for
    # are defined in the anonymous functions themselves)
    for Object in hosts:
        if ping(Object):
            execute_functions(Object)
    log(DEBUG, "Execution Completed")


logfile=open("logs/log.log","w+")
main()
