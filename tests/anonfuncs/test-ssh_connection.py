import fabric

# Connection testing
Cmd="cd && touch echoTESTING"
def Execute_ssh_shellcmd():
    Connection=fabric.Connection(host="10.0.0.204",user="flare",port=5656,
            connect_kwargs={'key_filename' : "/home/flare/.ssh/id_rsa"})
    Connection.open()
    Connection.run(Cmd)

Execute_ssh_shellcmd()
