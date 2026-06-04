#EN 

# Discord Username Availability Checker

A Python tool that automatically checks the availability of random Discord usernames and sends the results to a Discord channel via a bot.

---

## How It Works

1. Logs into Discord using Selenium (browser automation)
2. Generates random 4-character usernames (letters and digits)
3. Checks each username's availability through Discord's account settings page
4. Sends an embedded message to a Discord channel with the result (available / taken)
5. Repeats continuously

---

## Requirements

- Python 3.8+
- Google Chrome installed
- ChromeDriver (matching your Chrome version)

### Python dependencies

```
pip install selenium requests
```

---

## Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/your-repo.git
   cd your-repo
   ```

2. **Configure your credentials** in `usernamepublic.py`:
   ```python
   TOKEN = "your_discord_bot_token"
   CHANNEL_ID = "your_discord_channel_id"
   DISCORD_EMAIL = "your_discord_email"
   DISCORD_PASSWORD = "your_discord_password"
   ```

3. **Run the script**
   ```bash
   python usernamepublic.py
   ```

4. On first run, log in manually in the browser window that opens. After that, cookies are saved automatically.

---

## Notes

- Keep your credentials private — never commit real tokens or passwords to everyone
- Discord may rate-limit or flag automated account activity
- ChromeDriver must match your installed Chrome version: https://chromedriver.chromium.org/downloads

---
---

#RO

# Verificator de Disponibilitate Usernames Discord

Un bot Python care verifică automat disponibilitatea unor username-uri Discord generate aleatoriu și trimite rezultatele într-un canal Discord printr-un bot.

---

## Cum Funcționează

1. Se loghează în Discord folosind Selenium (automatizare browser)
2. Generează username-uri aleatoare de 4 caractere (litere și cifre)
3. Verifică disponibilitatea fiecărui username prin pagina de setări a contului Discord
4. Trimite un mesaj embed în canalul Discord cu rezultatul (disponibil / ocupat)
5. Repetă la infinit

---

## Cerințe

- Python 3.8+
- Google Chrome instalat
- ChromeDriver (compatibil cu versiunea ta de Chrome)

### Dependențe Python

```
pip install selenium requests
```

---

## Configurare

1. **Clonează repository-ul**
   ```bash
   git clone https://github.com/xtrnd/Discord-Username-Checker.git
   cd Discord-Username-Checker
   ```

2. **Completează credențialele** în `usernamepublic.py`:
   ```python
   TOKEN = "token-ul_botului_tau_discord"
   CHANNEL_ID = "id-ul_canalului_discord"
   DISCORD_EMAIL = "emailul_tau_discord"
   DISCORD_PASSWORD = "parola_ta_discord"
   ```

3. **Rulează scriptul**
   ```bash
   python usernamepublic.py
   ```

4. La prima rulare, loghează-te manual în fereastra de browser care se deschide. După aceea, cookie-urile sunt salvate automat.

---
Notițe

Ține credențialele private
Discord poate restricționa sau bloca activitatea automată a conturilor
ChromeDriver trebuie să fie compatibil cu versiunea de Chrome instalată: https://chromedriver.chromium.org/downloads
