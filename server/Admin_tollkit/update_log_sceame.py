"""
name:
date:
update the log settings to the setting in the file of the script argoment
"""
import socket, struct
import sys

if len(sys.argv) == 1:
    with open('D:\password_saver\server\log.yaml', 'r') as f:
        data_to_send = f.read()

    HOST = 'localhost'
    PORT = 9999
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('connecting...')
    s.connect((HOST, PORT))
    print('sending config...')
    s.send(struct.pack('>L', len(data_to_send)))
    s.send(data_to_send)
    s.close()
    print('complete')