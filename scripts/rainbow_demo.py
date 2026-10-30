import hashlib

# Kleine "Rainbow Table" aus den ersten 10000 Passwörtern von rockyou.txt vorberechnen
lookup = {}
with open("../rockyou.txt", "r", encoding="latin-1") as f:
    for i, line in enumerate(f):
        if i >= 10000:
            break
        pw = line.strip()
        md5_hash = hashlib.md5(pw.encode()).hexdigest()
        lookup[md5_hash] = pw

print(f"Lookup-Tabelle mit {len(lookup)} vorberechneten Hashes erstellt.\n")

# Test 1: ungesalzener MD5-Hash von "123456"
target_md5 = "e10adc3949ba59abbe56e057f20f883e"
if target_md5 in lookup:
    print(f"GEFUNDEN (ungesalzen): {target_md5} -> {lookup[target_md5]}")
else:
    print(f"NICHT GEFUNDEN (ungesalzen): {target_md5}")

# Test 2: gesalzener SHA1-Hash (kann hier nie gefunden werden, da Salt die Tabelle nutzlos macht)
target_salted = "6d39acd7dd8eacfe809e5d8bf51e58719ebb7c7e"
if target_salted in lookup:
    print(f"GEFUNDEN (gesalzen): {target_salted} -> {lookup[target_salted]}")
else:
    print(f"NICHT GEFUNDEN (gesalzen): {target_salted} - Salt verhindert Treffer in vorberechneter Tabelle")
