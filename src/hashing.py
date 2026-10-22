from pwdlib import PasswordHash

password_hash = PasswordHash.recommended()

hashed_password = password_hash.hash("MySecretPassword123")
is_valid = password_hash.verify("MySecretPassword123", hashed_password)

print(hashed_password)
print(is_valid)