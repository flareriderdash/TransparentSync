import subprocess


def execute(host):

    log(DEBUG, "Executing Vim_files.py for host: " + host.hostname)
    results=[]
    cmd={
        "vimrc out" : ["rsync","-u",'-i', '--rsh=ssh -p 5656',
            '/home/flare/.vimrc', host.hostname+':/home/flare/.vimrc'],
        ".vim out" : ["rsync","-u",'-r','-i', '--rsh=ssh -p 5656',
            '/home/flare/.vim',host.hostname+":/home/flare/.vim"],

        "vimrc in" : ["rsync","-u",'-i', '--rsh=ssh -p 5656',
             host.hostname+':/home/flare/.vimrc','/home/flare/.vimrc'],
        ".vim in" : ["rsync","-u",'-r','-i', '--rsh=ssh -p 5656',
            host.hostname+":/home/flare/.vim",'/home/flare/.vim']
    }

    # for every item in dictionary execute and log it
    for key in cmd:
        log(DEBUG,"Executing \"" +str(key) +"\" in vim_files.py")
        results.append(subprocess.check_output(cmd[key]))
    return results
