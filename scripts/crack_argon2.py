from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError
import time

ph = PasswordHasher()

target_hash = "$argon2id$v=19$m=65536,t=3,p=4$luvgcEvucAbyg0gI55SEBQ$ca+KKDymxm/E85+pgcjbxPGk1SvXcR/Vy4RUa78x1wg"

# Kleinere Wordlist nehmen (Argon2 ist langsam, volle rockyou.txt würde ewig dauern)
wordlist_path = "../rockyou.txt"
max_attempts = 5000  # reicht, da "123456" meist in den ersten Zeilen steht

start = time.time()
found = False
attempts = 0

with open(wordlist_path, "r", encoding="latin-1") as f:
    for line in f:
        attempts += 1
        if attempts > max_attempts:
            break
        password = line.strip()
        try:
            ph.verify(target_hash, password)
            print(f"GEKNACKT: '{password}' nach {attempts} Versuchen")
            found = True
            break
        except VerifyMismatchError:
            continue

elapsed = time.time() - start

if not found:
    print(f"Nicht geknackt nach {attempts} Versuchen.")

print(f"Dauer: {elapsed:.2f} Sekunden")
print(f"Geschwindigkeit: {attempts/elapsed:.2f} Versuche/Sekunde")
