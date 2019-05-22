#sr/bin/python3

import includes

def log(sstr):
    print(sstr)

def run_includes():
    global log
    for i in dir(includes):
        if "__" not in i:
            # Get pointers to functions included in module includes
            # Test to see if you can call anonfunctions and set external log
            # functions
            script=getattr(includes,i)
            # Test for setting attributes to imported modules  (log func 
            # defined above)
            setattr(script,"log",log)
            script.execute()

run_includes()
