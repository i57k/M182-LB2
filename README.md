<div align="center">
  <svg width="100%" viewBox="0 0 900 260" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Passwort-Sicherheit">
    <defs>
      <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
        <stop offset="0" stop-color="#13161c"/>
        <stop offset="1" stop-color="#1c2129"/>
      </linearGradient>
      <style>
        .mono { font-family: 'JetBrains Mono', 'Courier New', monospace; }
        .sans { font-family: 'Segoe UI', system-ui, sans-serif; }
        .plain  { animation: fade 8s ease-in-out infinite; }
        .hashed { animation: fadehash 8s ease-in-out infinite; }
        @keyframes fade {
          0%, 35% { opacity: 1; }
          45%, 90% { opacity: 0; }
          100% { opacity: 1; }
        }
        @keyframes fadehash {
          0%, 35% { opacity: 0; }
          45%, 90% { opacity: 1; }
          100% { opacity: 0; }
        }
        .cursor { animation: blink 1s steps(1) infinite; }
        @keyframes blink { 50% { opacity: 0; } }
        .shield { transform-origin: 820px 130px; animation: pulse 3s ease-in-out infinite; }
        @keyframes pulse {
          0%, 100% { transform: scale(1); opacity: .9; }
          50% { transform: scale(1.08); opacity: 1; }
        }
        .scan { animation: scanmove 8s ease-in-out infinite; }
        @keyframes scanmove {
          0%, 35% { opacity: 0; }
          40% { opacity: 1; }
          44% { transform: translateX(560px); opacity: 1; }
          46%, 100% { opacity: 0; transform: translateX(0); }
        }
      </style>
    </defs>
    <rect width="900" height="260" rx="20" fill="url(#bg)"/>
    <rect x="24" y="24" width="4" height="52" rx="2" fill="#f0a830"/>
    <text x="44" y="58" class="sans" font-size="30" font-weight="800" fill="#f7f6f2">Passwort-Sicherheit</text>
    <text x="44" y="90" class="sans" font-size="16" fill="#9aa3b2">Angriffe auf Hashing &amp; Verteidigungsstrategien · M182 LB2</text>
    <rect x="44" y="130" width="620" height="68" rx="12" fill="#0d0f14" stroke="#2a2f39" stroke-width="1.5"/>
    <text x="68" y="172" class="mono plain" font-size="26" fill="#2f9e6f">K7#mPx9!qLz2<tspan class="cursor" fill="#f0a830">▋</tspan></text>
    <text x="68" y="172" class="mono hashed" font-size="19" fill="#e5484d">52eadd82f8eeee484e875b496f54608c</text>
    <rect class="scan" x="46" y="132" width="3" height="64" fill="#f0a830" opacity="0"/>
    <g class="shield">
      <path d="M820 96 l34 14 v26 c0 26 -18 42 -34 50 c-16 -8 -34 -24 -34 -50 v-26 Z"
            fill="#1c2129" stroke="#f0a830" stroke-width="3"/>
      <path d="M808 132 l9 10 l18 -20" fill="none" stroke="#2f9e6f" stroke-width="4"
            stroke-linecap="round" stroke-linejoin="round"/>
    </g>
  </svg>
</div>

<br>

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
|  **[Dokumentation](Dokumentation/Dokumentation.md)** | **Klasse** (Lernressource) | Theorie zu Hashing, Salt, bcrypt und Argon2 · Angriffe mit Hashcat (Dictionary, Brute-Force, Rainbow Table) · Verteidigung mit Rate-Limiting, Fail2Ban, TOTP/2FA, Vaultwarden, Have I Been Pwned, Keycloak und testssl.sh · Reflexion · Quellen · Glossar · Selbsttests |
|  **[Projektplanung](Projektplanung/Projektplanung.md)** | **Lehrperson** | Ziele, Abgrenzung, Phasen, Arbeitspakete, Zeitplan, Arbeitsteilung, Zwischengespräch, Bewertungskriterien, Risiken, Reflexion · Troubleshooting-Historie |

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
