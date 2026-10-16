import hashlib
import bcrypt
from argon2 import PasswordHasher
import os
import json

test_passwords = {
    "schwach": "123456",
    "mittel": "Sommer2024",
    "stark": "K7#mPx9!qLz2",
}

ph = PasswordHasher()
results = {}

for label, pw in test_passwords.items():
    pw_bytes = pw.encode()
    salt = os.urandom(16)

    md5_hash = hashlib.md5(pw_bytes).hexdigest()
    sha1_hash = hashlib.sha1(pw_bytes).hexdigest()
    sha1_salted = hashlib.sha1(salt + pw_bytes).hexdigest()
    bcrypt_hash = bcrypt.hashpw(pw_bytes, bcrypt.gensalt()).decode()
    argon2_hash = ph.hash(pw)

    results[label] = {
        "passwort": pw,
        "md5": md5_hash,
        "sha1": sha1_hash,
        "sha1_gesalzen": sha1_salted,
        "salt_hex": salt.hex(),
        "bcrypt": bcrypt_hash,
        "argon2": argon2_hash,
    }

with open("hashes.json", "w") as f:
    json.dump(results, f, indent=2)

print("Hashes erzeugt und in hashes.json gespeichert.")
