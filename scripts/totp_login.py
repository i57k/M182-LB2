import pyotp

with open("totp_secret.txt", "r") as f:
    secret = f.read().strip()

totp = pyotp.TOTP(secret)

print("=== Login ===")
user_code = input("Gib den Code aus deiner Authenticator-App ein: ")

if totp.verify(user_code):
    print("2FA erfolgreich verifiziert - Login erlaubt.")
else:
    print("2FA fehlgeschlagen.")
