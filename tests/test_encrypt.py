from cryptography.fernet import Fernet
from src.key_manager import load_key
from src.encrypt import encrypt_file
from pathlib import Path
import pytest

SAMPLES = Path("samples")

def test_missing_file():
    key = load_key()
    f = Fernet(key)

    with pytest.raises(FileNotFoundError):
        encrypt_file("unknown.txt", key, f)


def test_encrypt_file():
    key = load_key()
    f = Fernet(key)

    filename = "test.txt"

    with open(SAMPLES / filename, "w") as file:
        file.write("Hello World")

    encrypt_file(filename, key, f)

    assert (SAMPLES / "test.txt.encrypted").exists()