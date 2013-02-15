#!/usr/bin/python
import paramiko
from scp import *
import sys

def createSSHClient(server, port, user, password):
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(server, port, user, password)
    return client

try:

    ssh = createSSHClient("127.0.0.1", 22, "sbehrens", "candiria7xx18")

except Exception as inst:

    print type(inst)
    print inst.args
    print inst
    
     
scp = SCPClient(ssh.get_transport())
transport = ssh.get_transport()
scp.put('/tmp/foobar', '/tmp/test')
channel = transport.open_session()
channel.exec_command("ls /tmp > /tmp/ididthis")
