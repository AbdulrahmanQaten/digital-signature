# crypto_utils.py
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
import os

KEY_FOLDER = "keys"

def generate_keys():
    os.makedirs(KEY_FOLDER, exist_ok=True)
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()

    with open(f"{KEY_FOLDER}/private.pem", "wb") as f:
        f.write(private_key)
    with open(f"{KEY_FOLDER}/public.pem", "wb") as f:
        f.write(public_key)

def sign_message(message: str) -> bytes:
    key = RSA.import_key(open(f"{KEY_FOLDER}/private.pem").read())
    h = SHA256.new(message.encode())
    signature = pkcs1_15.new(key).sign(h)
    return signature

def verify_signature(message: str, signature: bytes) -> bool:
    key = RSA.import_key(open(f"{KEY_FOLDER}/public.pem").read())
    h = SHA256.new(message.encode())
    try:
        pkcs1_15.new(key).verify(h, signature)
        return True
    except (ValueError, TypeError):
        return False
