# 🔐 FileEncrypt-Mini

A lightweight Python command-line application that securely encrypts and decrypts files using the Fernet symmetric encryption algorithm from the cryptography library.

## Features

- 🔒 Encrypt files securely using Fernet encryption
- 🔓 Decrypt encrypted files
- 🔑 Generate new encryption keys
- 🆔 KEYID verification to prevent using the wrong key
- 📝 Logging of encryption and decryption operations
- ✅ Unit tests using pytest
- 🎨 Colored terminal output using Colorama

---

## Project Structure

```
FileEncrypt-Mini/
│
├── keys/
│   └── encrypted.key
│
├── logs/
│   └── app.log
│
├── samples/
│   ├── note.txt
│   ├── note.txt.encrypted
│   └── note.txt.decrypted
│
├── src/
│   ├── encrypt.py
│   ├── decrypt.py
│   ├── key_manager.py
│   ├── logger.py
│   └── utils.py
│
├── tests/
│
├── main.py
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore
```

---

## Installation

### Clone the repository

```bash
git clone https://github.com/yourusername/FileEncrypt-Mini.git
cd FileEncrypt-Mini
```

### Create a virtual environment

Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

Linux/macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## Usage

Start the application:

```bash
python main.py
```

Menu:

```
1. Encrypt File
2. Decrypt File
3. Generate New Key
4. Exit
```

Place files to encrypt inside the `samples/` folder.

Encrypted files are saved as:

```
filename.ext.encrypted
```

Decrypted files are saved as:

```
filename.ext.decrypted
```

---

## KEYID Verification

Each encrypted file stores a short **KEYID** generated from the encryption key.

Before decrypting, the application verifies that the current key matches the stored KEYID.

This helps prevent accidental decryption attempts using the wrong encryption key.

---

## Running Tests

```bash
pytest
```

---

## Screenshots

Add screenshots of:

- Main menu
- Successful encryption
- Successful decryption
- Wrong key error

---

## Technologies Used

- Python 3
- cryptography (Fernet)
- Colorama
- pathlib
- logging
- hashlib
- pytest

---

## Future Improvements

- Password-protected encryption
- Drag-and-drop file selection
- GUI using Tkinter or CustomTkinter
- Encrypt multiple files at once
- Key backup and restore
- Support for folders

---

## License

This project is licensed under the MIT License.