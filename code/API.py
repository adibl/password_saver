"""
name:
date:
description
"""
import logging, logging.config
import socket
import threading
import os
import sys
sys.path.insert(0, "D:/adi/Documents/password_saver/code/Resorce") #FIXME: make this unesesery
import Resorce

import __logs
__logs.setup_logging()


HOST = '127.0.0.1'
PORT = 50007
CONN_LOG = "connect IP:{0} PORT:{1}"


def lisening():
    """
    :return:
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(5)
    while True:
        conn, addr = s.accept()
        logging.info(CONN_LOG.format(addr[0], str(addr[1])))
        threading.Thread(target=handle_client, args=(conn,)).start()



def handle_client(conn):
    """
    :param conn:
    :return:
    """
    data = conn.recv(1024)
    logging.debug("recv:" + data)
    responce = Resorce.process_request(data)
    conn.sendall(responce)
    logging.debug('sent:' + data)
    conn.close()

def main():
    lisening()


if __name__ == '__main__':
    main()
