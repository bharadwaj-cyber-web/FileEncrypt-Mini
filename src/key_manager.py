from cryptography.fernet import Fernet
from pathlib import Path
import hashlib



KEY_PATH = Path("keys/encrypted.key")



def get_key_id(key: bytes) -> str:
    """
    Generate a short unique identifier for an encryption key.

    Args:
        key: Fernet encryption key.

    Returns:
        First 16 characters of the SHA-256 hash of the key.
    """
    return hashlib.sha256(key).hexdigest()[:16]

def generate_key() -> bytes:
    """
    Generate a new Fernet encryption key and save it.

    Returns:
        The generated encryption key.
    """
    KEY_PATH.parent.mkdir(exist_ok=True)

    key = Fernet.generate_key()

    with KEY_PATH.open("wb") as key_file:
        key_file.write(key)

    return key


def load_key() -> bytes:
    """
    Load the existing encryption key.
    Generate one if it doesn't exist.
    """
    if not KEY_PATH.exists():
        return generate_key()

    with KEY_PATH.open("rb") as key_file:
        return key_file.read()