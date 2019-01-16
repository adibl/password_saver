"""
name:
date:
description
"""
import logging
import socket
import threading

import sys
sys.path.insert(0, "D:/adi/Documents/password_saver/code/Resorce") #FIXME: make this unesesery
import Resorce


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
        logger.log(logging.INFO, CONN_LOG.format(addr[0], str(addr[1])))
        threading.Thread(target=handle_client, args=(conn,)).start()



def handle_client(conn):
    """
    :param conn:
    :return:
    """
    data = conn.recv(1024)
    logger.log(logging.INFO, "RECV:" + data)
    responce = Resorce.process_request(data)
    conn.sendall(responce)
    conn.close()

def main():
    lisening()


if __name__ == '__main__':
    global logger
    logger = logging.getLogger('simple_example')
    logger.setLevel(logging.DEBUG)

    # create console handler and set level to debug
    fh = logging.FileHandler('spam.log')
    fh.setLevel(logging.DEBUG)

    # create formatter
    formatter = logging.Formatter('%(thread)d-%(levelname)s-%(message)s')

    # add formatter to ch
    fh.setFormatter(formatter)

    # add ch to logger
    logger.addHandler(fh)
    main()
