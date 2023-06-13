import hashlib

def generate_hashed_password(password):
    # Hash the password using SHA-256
    sha256_hash = hashlib.sha256()
    sha256_hash.update(password.encode('utf-8'))
    hashed_password = sha256_hash.hexdigest()
    return hashed_password

# Example usage
password = "123"
hashed_password=hashlib.sha256(password.encode('utf-8')).hexdigest()  

print(hashed_password)

