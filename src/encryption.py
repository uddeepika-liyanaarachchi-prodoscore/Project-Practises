from cryptography.fernet import Fernet

# 1. Encryption Key- generate 
secret_key = Fernet.generate_key()
cipher_suite = Fernet(secret_key)

# 2. Encrypting
sensitive_data = "CreditCard: 4532-1234-5678-9012"
print("Before Encrption :", sensitive_data)
encrypted_text = cipher_suite.encrypt(sensitive_data.encode())

print("After Encrypted:", encrypted_text)

# 3. Decrypting
decrypted_text = cipher_suite.decrypt(encrypted_text).decode()
print("Decrypted Value:", decrypted_text)