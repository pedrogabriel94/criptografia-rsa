from socket import *
import crypto as c
import pickle

host = 'localhost'
port = 60001
sock = socket(AF_INET, SOCK_STREAM)
sock.bind((host, port))
sock.listen(1)

c.key_generator()

while True:
    print('Esperando conexão...')
    connection, address = sock.accept()
    print('Conexão estabelecida com o host {} na porta {}'.format(address[0], address[1]))
    received_msg = connection.recv(2048)
    
    msg = pickle.loads(received_msg)

    keyPrivate = c.returnKeyPrivate()

    a = c.decryption(msg, keyPrivate)

    print('Mensagem recebida: ', msg)
    print('Mensagem decriptada: ', a)