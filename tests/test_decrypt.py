from cryptography.fernet import Fernet
from src.key_manager import load_key
from src.encrypt import encrypt_file
from src.decrypt import decrypt_file
from pathlib import Path

SAMPLES = Path("samples")


def test_decrypt_file():
    key = load_key()
    f = Fernet(key)

    filename = "test.txt"

    with open(SAMPLES / filename, "w") as file:
        file.write("Hello World")

    # Encrypt using current key
    encrypt_file(filename, key, f)

    # Now decrypt
    decrypt_file(filename, f)

    with open(SAMPLES / "test.txt.decrypted") as file:
        data = file.read()

    assert data == "Hello World"