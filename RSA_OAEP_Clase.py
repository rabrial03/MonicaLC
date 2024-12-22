from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Hash import SHA256
from Crypto.Cipher.PKCS1.OAEP import MGF1

fichero_pub = "/home/monica/Desktop/cripto-main/Practica/claveprivada-RSA_desc_oaep.pem"
with open(fichero_pub, 'r') as f:
    pubKey = RSA.import_key(f.read())

mensaje = bytes.fromhex("e2cff885901a5449e9c448ba5b948a8c4ee377152b3f152b3f1acfa0148fb3a426db72")
cipher = PKCS1_OAEP.new(pubKey, mgfunc=MGF1(SHA256), hashAlgo=SHA256)
text_cifrado = cipher.encrypt(mensaje)
print("Cifrado:", test_cifrado.hex())

print("--------------------------------------------------")

