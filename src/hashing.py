import hashlib

# password
password = "MySecretPassword123"

# SHA-256- Hashing
hash_object = hashlib.sha256(password.encode())
hashed_password = hash_object.hexdigest()

print("Original Password:", password)
print("Hashed Output    :", hashed_password)