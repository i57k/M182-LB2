import pyotp
import time

# Geheimer Schlüssel wird einmalig generiert (würde normalerweise beim Setup
# zwischen Server und App geteilt, z. B. per QR-Code)
secret = pyotp.random_base32()
print(f"Geheimer Schluessel (Secret): {secret}")

totp = pyotp.TOTP(secret)

# Aktuellen gueltigen Code anzeigen
current_code = totp.now()
print(f"Aktuell gueltiger TOTP-Code: {current_code}")

# Simulierter Login: Benutzer gibt Passwort UND TOTP-Code ein
print("\n=== Simulierter Login ===")
user_code = input("Gib den aktuellen TOTP-Code ein: ")

if totp.verify(user_code):
    print("2FA erfolgreich verifiziert - Login erlaubt.")
else:
    print("2FA fehlgeschlagen - falscher oder abgelaufener Code.")

# Demonstration: Code ist nur fuer ein kurzes Zeitfenster gueltig (Standard 30s)
print(f"\nDieser Code ist nur fuer {totp.interval} Sekunden gueltig.")
