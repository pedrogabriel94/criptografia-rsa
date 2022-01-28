from socket import *
import crypto as c
import pickle

host = 'localhost'
port = 60001

sock = socket(AF_INET, SOCK_STREAM)
sock.connect((host, port))
print('Conexão com receptor estabelecida!')

msg = input('Digite uma mensagem: ')

keyPublic = c.returnKeyPublic() 

msgEncriptada = c.encryption(msg, keyPublic)

print('Mensagem enviada: ', msgEncriptada)
print('Mensagem encriptada: ', msg)

msgEncriptada = pickle.dumps(msgEncriptada)

sock.send(msgEncriptada)

sock.close()

print('Conexão encerrada!')
