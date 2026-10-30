# M182 LB2 – Passwort-Sicherheit

**Angriffe auf Hashing und mögliche Verteidigungsstrategien – Salt, moderne Verfahren wie bcrypt oder Argon2, Passwort-Policy, Rate-Limiting, 2FA**

| | |
|---|---|
| **Autoren** | Thasleem Aakib, Schubert Diago |
| **Klasse** | PE23F |
| **Modul** | M182 – Systemsicherheit implementieren |
| **Lehrperson** | Kemper Stefan |
| **Art der Arbeit** | LB2 – Projektarbeit (Dokumentation) |

---

## Die zwei Dokumente

| Dokument | Für wen? | Inhalt |
|---|---|---|
| 📘 **[Dokumentation](Dokumentation/Dokumentation.md)** | **Klasse** (Lernressource) | Theorie zu Hashing, Salt, bcrypt und Argon2 · Angriffe mit Hashcat (Dictionary, Brute-Force, Rainbow Table) · Verteidigung mit Rate-Limiting, Fail2Ban, TOTP/2FA, Vaultwarden, Have I Been Pwned, Keycloak und testssl.sh · Reflexion · Quellen · Glossar · Selbsttests |
| 📋 **[Projektplanung](Projektplanung/Projektplanung.md)** | **Lehrperson** | Ziele, Abgrenzung, Phasen, Arbeitspakete, Zeitplan, Arbeitsteilung, Zwischengespräch, Bewertungskriterien, Risiken, Reflexion · Troubleshooting-Historie |

## Direkt zu den Kapiteln

**Dokumentation (Klasse)**

1. [Grundlagen – Hashing, Salt, bcrypt, Argon2, Passwort-Policy](Dokumentation/Dokumentation.md#kapitel-1--grundlagen-hashing-salt-bcrypt-argon2-und-passwort-policy)
2. [Testumgebung – Werkzeuge, Aufbau, Testpasswörter](Dokumentation/Dokumentation.md#kapitel-2--testumgebung-werkzeuge-aufbau-und-testpasswörter)
3. [Angriffe – Dictionary, Brute-Force, Rainbow Tables](Dokumentation/Dokumentation.md#kapitel-3--angriffe-dictionary-brute-force-und-rainbow-tables)
4. [Verteidigung – von Salt bis zum Security-Audit](Dokumentation/Dokumentation.md#kapitel-4--verteidigung-von-salt-bis-zum-security-audit)
5. [Reflexion und Fazit](Dokumentation/Dokumentation.md#kapitel-5--reflexion-und-fazit)
6. [Quellenverzeichnis](Dokumentation/Dokumentation.md#kapitel-6--quellenverzeichnis)
7. [Glossar](Dokumentation/Dokumentation.md#kapitel-7--glossar)

**Projektplanung (Lehrperson)**

- [Ziele](Projektplanung/Projektplanung.md#3-ziele) · [Zeitplan und Arbeitsjournal](Projektplanung/Projektplanung.md#7-zeitplan-und-arbeitsjournal) · [Arbeitsteilung](Projektplanung/Projektplanung.md#8-arbeitsteilung) · [Zwischengespräch](Projektplanung/Projektplanung.md#9-zwischengespräch-mit-der-lehrperson) · [Troubleshooting](Projektplanung/Projektplanung.md#14-troubleshooting-historie)

## Ergebnisse auf einen Blick

| Test | Ergebnis |
|---|---|
| MD5-Hash von `123456` | in **unter 1 Sekunde** geknackt |
| Brute-Force gegen MD5 | ca. **400 Millionen** Versuche pro Sekunde (nur CPU) |
| Zufälliges 12-Zeichen-Passwort als MD5 | ca. **43 Millionen Jahre** Brute-Force |
| bcrypt / Argon2 | nur noch **39 bzw. 10** Versuche pro Sekunde |
| Rate-Limiting, Fail2Ban, Keycloak | Sperre nach **3 Fehlversuchen** |
| HIBP-Check | `Stefan123!` wurde **2511-mal** in Datenlecks gefunden |

## Aufbau des Repositorys

```
M182-LB2/
├── README.md                          Diese Übersicht
├── Dokumentation/
│   ├── Dokumentation.md               Lernressource für die Klasse
│   └── images/                        69 Abbildungen
├── Projektplanung/
│   ├── Projektplanung.md              Projektplanung und Troubleshooting
│   └── images/                        13 Abbildungen
└── scripts/                           Alle Python-Skripte und Test-Hashes
    ├── generate_hashes.py             Erzeugt MD5-, SHA-1-, bcrypt- und Argon2-Hashes
    ├── crack_argon2.py                Dictionary-Attacke gegen Argon2
    ├── rainbow_demo.py                Prinzip einer vorberechneten Hash-Tabelle
    ├── rate_limit_interactive.py      Login mit Sperre nach 3 Fehlversuchen
    ├── rate_limit_demo.py             Automatischer Test des Rate-Limitings
    ├── totp_demo.py                   TOTP-Grundlagen
    ├── totp_setup.py                  TOTP-Secret und QR-Code für die Authenticator-App
    ├── totp_login.py                  Login mit Code aus der Authenticator-App
    ├── hibp_check.py                  Abgleich mit Have I Been Pwned (k-Anonymity)
    └── *.txt, hashes.json             Test-Hashes der drei Testpasswörter
```

## Skripte selbst ausprobieren

```bash
cd scripts
python3 -m venv venv
source venv/bin/activate
pip install bcrypt argon2-cffi pyotp qrcode[pil] requests
python3 generate_hashes.py
```

Für die Angriffe wird zusätzlich [Hashcat](https://hashcat.net) und die Wordlist `rockyou.txt` im Hauptordner benötigt. Die Wordlist ist wegen ihrer Grösse (134 MB) nicht im Repository enthalten.

> [!IMPORTANT]
> Alle Angriffe wurden ausschliesslich gegen **selbst erstellte Test-Passwörter** in einer **eigenen, isolierten Testumgebung** durchgeführt. Das Knacken fremder Passwörter oder Angriffe auf fremde Systeme sind strafbar (Art. 143<sup>bis</sup> StGB).
