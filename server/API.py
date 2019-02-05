"""
name: adi bleyer1
date: 1.18.19
the main file of the server.
runs the server and wrap up everything.
"""
import logging
import logging.config
import re
import socket
import sys
import threading
from request import Request
from server.Autentication.request import AuthenticatedRequest
from server.HTTPtolls import *
import Resorce
import __logs



HOST = '127.0.0.1'
PORT = 50007
CONN_LOG = "connect IP:{0} PORT:{1}"


def handle_logging():
    """
    create tread that listen and auto-cange log config on run
    :return: tread object
    """
    # FIXME: move to __logs file
    __logs.setup_logging()
    logging.info('start logging changes server')
    return logging.config.listen(9999).start()



def lisening():
    """
    the main propg of the server. listen for clients
    :return: None
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(10)
    while True:
        conn, addr = s.accept()
        logging.info(CONN_LOG.format(addr[0], str(addr[1])))
        threading.Thread(target=handle_client, args=(conn,)).start()


def receive(client_socket, func=lambda data: not re.search(".*\r\n\r\n(.*\r\n)?", data)): #FIXME: cant get requests with body
    """
    :param func: the exit funcsion of the while loop.
    :param client_socket: the comm socket
    :return: the data thet was recived from the socket
    """
    data = ""
    while func(data):
        data += client_socket.recv(1024)
    logging.debug("RECV:" + data)
    return data.replace('\r\n', '\n')


def handle_client(conn):
    """
    :param conn: the socket of the client
    :return: None
    """
    request = receive(conn)
    code = Request.validate(request)
    if code == OK:
        code = AuthenticatedRequest.validate(request)
        if code == OK:
            if Resorce.ResorceRequest.IsResorceURL(request):
                responce = Resorce.process_request(Resorce.ResorceRequest(request))
            else:
                responce = Responce.not_found()
        else:
           responce = Responce.validate_erors(code)
    else:
        responce = Responce.validate_erors(code)
    conn.sendall(responce)
    logging.debug('sent:' + responce)
    conn.close()

def main():
    trd = handle_logging()
    lisening()
    trd.stopListening()
    trd.join()


if __name__ == '__main__':
    main()
