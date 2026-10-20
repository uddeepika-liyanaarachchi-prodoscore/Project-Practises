import bcrypt

# Password Hashing
user_password = "MySuperSecretPassword@2026"

# convert Password to bytes
password_bytes = user_password.encode("utf-8")

# Salt generation
salt = bcrypt.gensalt(rounds=12)

# Hashing using salt and pw
hashed_password = bcrypt.hashpw(password_bytes, salt)

print("--- REGISTRATION ---")
print(f"Original Password : {user_password}")
print(f"Generated Salt    : {salt.decode('utf-8')}")
print(f"PW converted bytes: {password_bytes}")
print(f"Hashed Output     : {hashed_password.decode('utf-8')}")