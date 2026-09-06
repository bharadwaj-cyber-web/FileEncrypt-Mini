from pathlib import Path
from src.utils import success,info
from cryptography.fernet import InvalidToken
from src.key_manager import load_key, get_key_id
from src.logger import logger
from cryptography.fernet import Fernet

SAMPLES = Path("samples")

def decrypt_file(filename: str, f: Fernet) -> None:
    """
    Decrypt an encrypted file after verifying the KEYID.

    Reads the KEYID stored in the encrypted file, compares it with
    the current key, and decrypts the file only if they match.

    Args:
        filename: Original filename without the `.encrypted` extension.
        f: Fernet object used for decryption.

    Raises:
        FileNotFoundError: If the encrypted file does not exist.
        ValueError: If the KEYID does not match the current key.
        InvalidToken: If the encrypted data is corrupted or the key is invalid.
    """

    encrypted_filepath = SAMPLES / (filename + ".encrypted")

    

    if not encrypted_filepath.exists():
        raise FileNotFoundError



    with encrypted_filepath.open("rb") as file:
        key_line = file.readline().decode().strip()
        
        
        if not key_line.startswith("KEYID:"):
            raise ValueError("Invalid encrypted file format.")

        stored_key_id = key_line.replace("KEYID:", "")
        encrypted_data = file.read()

    current_key = load_key()

    current_key_id = get_key_id(current_key)

    if stored_key_id != current_key_id:
        raise ValueError(
            "This file was encrypted using a different key.\n"
            "Restore the original key to decrypt it."
        )


    
    decrypted_data = f.decrypt(encrypted_data)

    decrypted_filepath = SAMPLES / (filename + ".decrypted")

    with decrypted_filepath.open("wb") as file:
        file.write(decrypted_data)


    success("File decrypted successfully")
    info(f"Decrypted file saved as {decrypted_filepath.name}")
    logger.info(f"Decrypted file: {filename}")