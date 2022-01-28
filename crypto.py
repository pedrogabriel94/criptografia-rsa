from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import pickle
import base64


def key_generator():
    key = RSA.generate(2048)

    private_key = key.export_key()
    public_key = key.public_key().export_key()

    private = open('chaves/private.txt', 'wb')
    public = open('chaves/public.txt', 'wb')

    private.write(private_key)
    public.write(public_key)

    private.close()
    public.close()


def encryption(msg, public_key):
    msg = pickle.dumps(msg)
    key = RSA.importKey(public_key)
    cipher_rsa = PKCS1_OAEP.new(key)
    c_msg = cipher_rsa.encrypt(msg)

    return base64.b64encode(c_msg)


def decryption(msg, private_key):
    msg = base64.b64decode(msg)
    key = RSA.importKey(private_key)
    cipher_rsa = PKCS1_OAEP.new(key)
    c_msg = cipher_rsa.decrypt(msg)

    return pickle.loads(c_msg)

def returnKeyPublic():
    f = open('chaves/public.txt', 'r')
    key = RSA.importKey(f.read())

    public_key = key.publickey().exportKey()

    f.close()

    return public_key

def returnKeyPrivate():
    f = open('chaves/private.txt', 'r')
    key = RSA.importKey(f.read())

    private_key = key.exportKey()

    f.close()

    return private_key


