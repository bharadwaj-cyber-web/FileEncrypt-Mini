from cryptography.fernet import Fernet,InvalidToken
from src.key_manager import load_key, generate_key ,get_key_id
from src.encrypt import encrypt_file
from src.decrypt import decrypt_file
from src.utils import banner,error,success
from src.logger import logger


def main():
    banner()

    key = load_key()
    f = Fernet(key)

    while True:
        print("\n" + "=" * 45)
        print(" FileEncrypt Mini ")
        print("=" * 45)

        print("1. Encrypt File")
        print("2. Decrypt File")
        print("3. Generate New Key")
        print("4. Exit")
        print("=" * 45)

        choice = input("Enter your choice: ")

        if choice == "1":
            filename = input("Enter filename: ").strip()

            if not filename:
                error("File name cannot be empty")
                continue

            try:
                current_key = load_key()
                f = Fernet(current_key)
                encrypt_file(filename,current_key,f)
            except FileNotFoundError:
                error("File not found. Place file inside sample folder")
            except Exception as e:
                error(str(e))
                logger.exception("Unexpected Error")

        elif choice == "2":
            filename = input("Enter original filename: ").strip()

            current_key = load_key()
            f = Fernet(current_key)
            print(f"Current Key ID: {get_key_id(current_key)}")
            try:
                decrypt_file(filename, f)
            except FileNotFoundError:
                error("encrypted file not found.")
                logger.error(f"File not found: {filename}")
            except ValueError as e:
                error(str(e))
                logger.error(f"Decryption failed for '{filename}': {e}")
            except InvalidToken:
                error("Wrong encryption key!")
                logger.error(f"Wrong key used for: {filename}")
                print("This file was encrypted using a different key.")
            except Exception as e:
                error(str(e))
                logger.exception("Unexpected error")


        elif choice == "3":

            confirm = input(
            "Generating a new key will make old encrypted files unreadable.\nContinue? (y/n): "
            ).lower()

            if confirm == "y":
                generate_key()
                key = load_key()
                f = Fernet(key)
                success("New key generated successfully!")
                logger.info("Generated a new encryption key")
            else:
                print("Operation cancelled.")


        elif choice == "4":
            print("Thank you for using FileEncrypt-Mini!")
            break

        else:
            error("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()