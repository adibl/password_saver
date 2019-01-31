"""
name: adi bleyer1
date: 1.18.19
the main file of the server.
runs the server and wrap up everything.
"""
import logging
import logging.config
import socket
import sys
import threading

sys.path.insert(0, "D:/adi/Documents/password_saver/server/Resorce") #FIXME: make this unesesery
import Resorce
import __logs



HOST = '127.0.0.1'
PORT = 50008
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


def receive(client_socket, func=lambda data: "\r\n\r\n" not in data):
    """
    :param func: the exit funcsion of the while loop.
    :param client_socket: the comm socket
    :return: the data thet was recived from the socket
    """
    data = ""
    while func(data):
        data += client_socket.recv(1024)
    logging.debug("RECV:" + data)
    return data


def handle_client(conn):
    """
    :param conn: the socket of the client
    :return: None
    """
    data = receive(conn)
    responce = Resorce.process_request(data)
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
