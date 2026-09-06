from pathlib import Path
from src.utils import success, info
from src.key_manager import get_key_id
from src.logger import logger
from cryptography.fernet import Fernet


SAMPLES = Path("samples")

def encrypt_file(filename: str, key: bytes, f: Fernet) -> None:
    """
    Encrypt a file using the provided Fernet key.

    Reads a file from the samples directory, encrypts its contents,
    stores the KEYID in the output file, and saves it with the
    `.encrypted` extension.

    Args:
        filename: Name of the file to encrypt.
        key: Encryption key in bytes.
        f: Fernet object used for encryption.

    Raises:
        FileNotFoundError: If the input file does not exist.
    """
    filepath = SAMPLES / filename

    key_id = get_key_id(key)

    if not filepath.exists():
        raise FileNotFoundError(f"{filename} not found in {SAMPLES}")

    with open(filepath, "rb") as file:
        data = file.read()

    encrypted_data = f.encrypt(data)

    encrypted_filename = filepath.with_suffix(filepath.suffix + ".encrypted")

    with encrypted_filename.open("wb") as file:
        file.write(f"KEYID:{key_id}\n".encode())
        file.write(encrypted_data)

    success(f"{filename} encrypted successfully")
    
    info(f"Saved as {encrypted_filename.name}")

    logger.info(f"Encrypted file: {filename}")

