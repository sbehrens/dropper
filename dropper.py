#!/usr/bin/python
import paramiko
from scp import *
import sys

def createSSHClient(server, port, user, password):
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(server, port, user, password, timeout=3)
    return client

try:

    ssh = createSSHClient("10.40.122.172", 22, "sbehrens", "candiria718")

except Exception as inst:

    # print hostname with error
    print type(inst)
    print inst.args
    print inst
    
     
scp = SCPClient(ssh.get_transport())
transport = ssh.get_transport()
try:
scp.put('/tmp/foobar', '/tmp/test')
channel = transport.open_session()
channel.exec_command("ls /opt > /tmp/ididthis")
