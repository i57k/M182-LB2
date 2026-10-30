import pyotp
import qrcode

secret = pyotp.random_base32()
print(f"Secret (fuer Authenticator-App): {secret}")

with open("totp_secret.txt", "w") as f:
    f.write(secret)

totp = pyotp.TOTP(secret)
uri = totp.provisioning_uri(name="aakibdiago@m182-lb2", issuer_name="M182-LB2-PasswortSicherheit")

print(f"\nURI: {uri}\n")

qr = qrcode.QRCode()
qr.add_data(uri)
qr.print_ascii(invert=True)
