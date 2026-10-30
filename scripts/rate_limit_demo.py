import time
from datetime import datetime

correct_password = "MeinSicheresPasswort123"
MAX_ATTEMPTS = 3
LOCKOUT_SECONDS = 10

failed_attempts = 0
locked_until = 0

def timestamp():
    return datetime.now().strftime("%H:%M:%S")

def login(password_input):
    global failed_attempts, locked_until
    now = time.time()

    if now < locked_until:
        remaining = int(locked_until - now)
        print(f"[{timestamp()}] GESPERRT - noch {remaining}s warten (Eingabe war: '{password_input}')")
        return False

    if password_input == correct_password:
        print(f"[{timestamp()}] LOGIN ERFOLGREICH mit Passwort '{password_input}'")
        failed_attempts = 0
        return True
    else:
        failed_attempts += 1
        print(f"[{timestamp()}] Falsches Passwort '{password_input}' - Versuch {failed_attempts}/{MAX_ATTEMPTS}")
        if failed_attempts >= MAX_ATTEMPTS:
            locked_until = now + LOCKOUT_SECONDS
            print(f"[{timestamp()}] >>> SPERRE AKTIVIERT fuer {LOCKOUT_SECONDS} Sekunden <<<")
        return False


print(f"[{timestamp()}] === Test startet ===\n")

login("falsch1")
time.sleep(1)
login("falsch2")
time.sleep(1)
login("falsch3")
time.sleep(1)

print(f"\n[{timestamp()}] >>> Versuche JETZT das KORREKTE Passwort waehrend der Sperre <<<")
login(correct_password)

print(f"\n[{timestamp()}] Warte {LOCKOUT_SECONDS} Sekunden, bis Sperre abgelaufen ist...")
time.sleep(LOCKOUT_SECONDS + 1)

print(f"\n[{timestamp()}] >>> Versuche KORREKTES Passwort NACH Ablauf der Sperre <<<")
login(correct_password)
