import hashlib
import requests

def check_pwned(password):
    sha1 = hashlib.sha1(password.encode()).hexdigest().upper()
    prefix, suffix = sha1[:5], sha1[5:]

    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    response = requests.get(url)

    hashes = (line.split(':') for line in response.text.splitlines())
    for h, count in hashes:
        if h == suffix:
            return int(count)
    return 0

pw = input("Passwort zum Pruefen eingeben: ")
count = check_pwned(pw)

if count:
    print(f"WARNUNG: Dieses Passwort wurde {count} mal in bekannten Datenlecks gefunden!")
else:
    print("Dieses Passwort wurde in keinem bekannten Leak gefunden.")
