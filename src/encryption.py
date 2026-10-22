from cryptography.fernet import Fernet

secret_key = Fernet.generate_key()
cipher_suite = Fernet(secret_key)

sensitive_data = "CreditCard: 4532-1234-5678-9012"
print("Before Encrption :", sensitive_data)
encrypted_text = cipher_suite.encrypt(sensitive_data.encode())

print("After Encrypted:", encrypted_text)

decrypted_text = cipher_suite.decrypt(encrypted_text).decode()
print("Decrypted Value:", decrypted_text)