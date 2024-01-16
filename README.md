# password_manager
Password Manager Code Description

Overview

The Password Manager is a Python application designed to securely manage and store usernames and passwords. It incorporates AES encryption to ensure the confidentiality of sensitive information. Below are the key features of the code:

main.py

Features:
User-Friendly Menu:
The script provides a user-friendly menu for interacting with the password manager.
Options include listing usernames, storing new credentials, accessing passwords, and exiting the program.
Master Password Protection:
Users are required to enter a master password to access the password manager.
The master password is hashed and stored in master_hash.txt for verification.
Data Storage:
Usernames and passwords are stored in JSON files within a dedicated /data directory.
The script creates the directory if it doesn't exist.
Error Handling:
The code includes error handling for incorrect master passwords and username duplicates.
Usage:
Run main.py.
Enter the master password.
Choose an option from the menu to list usernames, store new credentials, access passwords, or exit.
pass_manager.py

Features:
AES Encryption:
The module provides functions for encrypting and decrypting data using the Advanced Encryption Standard (AES).
AES keys and IVs are randomly generated for each entry.
Data Encryption and Decryption:
encrypt_aes: Encrypts and stores username and password data in JSON files.
decrypt_aes: Decrypts stored data when accessing passwords.
Data Integrity:
The code ensures the integrity of encrypted data by using PKCS7 padding.
Password Manager Class:
The PasswordManager class is responsible for storing and accessing encrypted data.
Usage:
The PasswordManager class is instantiated with a username and password.
store_data: Stores encrypted data for a new username or updates existing data.
access_password: Decrypts and retrieves the password for a given username.
Security Considerations:

The master password is securely hashed and stored, enhancing the overall security of the application.
AES encryption with randomly generated keys and IVs is employed for secure storage and retrieval of sensitive information.
This Password Manager is a lightweight yet effective solution for users seeking a secure way to manage their credentials.
