"""
name:
date:
update the log settings to the setting in the file of the script argoment
"""
import socket, struct
import yaml
import sys
import logging.config
import logging

if len(sys.argv) == 2:
    with open(sys.argv[1], 'r') as f:
        data_to_send = yaml.safe_load(f.read()) #FIXME: transfor to str taht is good for recv


    # check if the format is good
    logging.config.dictConfig(data_to_send)
    logging.info('aa')


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