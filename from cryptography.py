from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives.hashes import SHA512
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend

# Clave maestra simulada (esto normalmente se recupera del keystore)
master_key = bytes.fromhex("cifrado-sim-aes-256".encode().hex())  # Esto es un ejemplo, deberás usar la real.

# ID de dispositivo en hexadecimal
device_id = bytes.fromhex("e43bb4067cbcfab3bec54437b84bef4623e345682d89de9948fbb0afedc461a3")

# Generar clave derivada usando HKDF
derived_key = HKDF(
    algorithm=SHA512(),
    length=32,  # La longitud de clave AES (256 bits = 32 bytes)
    salt=None,  # Sin salt
    info=device_id,  # Usamos el identificador del dispositivo
    backend=default_backend()
).derive(master_key)

# Imprimir la clave derivada en hexadecimal
print("Clave derivada:", derived_key.hex())
