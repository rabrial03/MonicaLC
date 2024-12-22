from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.serialization import load_pem_private_key
from cryptography.hazmat.backends import default_backend

# Cargar clave privada RSA
with open("/home/monica/Downloads/cripto-main/Practica/clave-rsa-oaep-priv.pem", "rb") as key_file:
    private_key = load_pem_private_key(key_file.read(), password=None, backend=default_backend())

# Especificar la ruta "/home/monica/Downloads/cripto-main/Practica/clave-rsa-oaep-priv.pem" 
with open("/home/monica/Downloads/cripto-main/Practica/clave-rsa-oaep-priv.pem", "rb") as key_file:
    private_key = load_pem_private_key(key_file.read(), password=None, backend=default_backend())


# Mensaje a firmar
message = b"El equipo est\xc3\xa1 preparado para seguir con el proceso, necesitaremos m\xc3\xa1s recursos."

# Firmar el mensaje
signature = private_key.sign(
    message,
    padding.PKCS1v15(),
    hashes.SHA256()
)

# Mostrar firma en hexadecimal
print("Firma RSA PKCS#1 v1.5 (hex):", signature.hex())
