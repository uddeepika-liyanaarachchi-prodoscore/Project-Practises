import bcrypt

user_password = "MySuperSecretPassword@2026"

password_bytes = user_password.encode("utf-8")

salt = bcrypt.gensalt(rounds=12)

hashed_password = bcrypt.hashpw(password_bytes, salt)

print("--- REGISTRATION ---")
print(f"Original Password : {user_password}")
print(f"Generated Salt    : {salt.decode('utf-8')}")
print(f"PW converted bytes: {password_bytes}")
print(f"Hashed Output     : {hashed_password.decode('utf-8')}")