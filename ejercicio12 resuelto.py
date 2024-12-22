from Crypto.Cipher import AES
import base64

key = bytes.fromhex("E2CFF885901B3449E9C448BA5B948A8C4EE322152B3F1ACFA0148FB3A426DB74")
nonce = base64.b64decode("9Yccn/f5nJJhAt2S")
plaintext = "He descubierto el error y no volveré a hacerlo mal".encode('utf-8')
cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
ciphertext, tag = cipher.encrypt_and_digest(plaintext)
print("Nonce (hex):", nonce.hex())
print("Texto cifrado (hex):", ciphertext.hex())
print("Texto cifrado (base64):", base64.b64encode(ciphertext).decode('utf-8'))
print("Etiqueta de autenticación (hex):", tag.hex())
print("Etiqueta de autenticación (base64):", base64.b64encode(tag).decode('utf-8'))
