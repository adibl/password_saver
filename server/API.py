"""
name: adi bleyer1
date: 1.18.19
the main file of the server.
runs the server and wrap up everything.
"""
import logging.config
import re
import socket
import threading
import ssl

from Resorce.request import ResorceRequest
from UserManagment.request import RegisterRequest, LoginRequests, ResetRequest
from __logs import handle_logging
from request import Request
from server.Autentication.request import AuthenticatedRequest
from server.HTTPtolls import *

HOST = '0.0.0.0'
PORT = 50007
CONN_LOG = "connect IP:{0} PORT:{1}"


def lisening():
    """
    the main propg of the server. listen for clients
    :return: None
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s = ssl.wrap_socket(s, ssl_version=ssl.PROTOCOL_SSLv23, server_side=True, certfile=r'C:\Users\adi\openssl\server.cert', keyfile=r'C:\Users\adi\openssl\private.pem')
    s.bind((HOST, PORT))
    s.listen(10)
    while True:
        conn, addr = s.accept()
        logging.info(CONN_LOG.format(addr[0], str(addr[1])))
        threading.Thread(target=handle_client, args=(conn,)).start()


def receive(client_socket, func=lambda data: not re.search(".*\r\n\r\n(.*\r\n\r\n)?", data)):
    """
    :param func: the exit funcsion of the while loop.
    :param client_socket: the comm socket
    :return: the data thet was recived from the socket
    """
    data = ""
    while not re.search(".*\r\n\r\n", data):
        data += client_socket.recv(2048)
    logging.debug("RECV:" + data)
    return data.replace('\r\n', '\n')  # FIXME: ergent!!!!!


def handle_request(cl, request):
    code = cl.validate(request)
    if code == OK:
        resorce_request = cl(request)
        responce = resorce_request.process_request()
    else:
        responce = Responce.validate_erors(code)
    return responce


def handle_client(conn):
    """
    :param conn: the socket of the client
    :return: None
    """
    request = receive(conn)
    code = Request.validate(request)
    if code == OK:
        if RegisterRequest.IsResorceURL(request):
            responce = handle_request(RegisterRequest, request)
        elif ResetRequest.IsResorceURL(request):
            responce = handle_request(ResetRequest, request)
        else:
            code = AuthenticatedRequest.validate(request)
            if code == OK:
                if ResorceRequest.IsResorceURL(request):
                    responce = handle_request(ResorceRequest, request)
                elif LoginRequests.IsResorceURL(request):
                    responce = handle_request(LoginRequests, request)
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
