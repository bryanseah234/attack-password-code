# attackpassword
> ZIP file password cracker — brute force and dictionary attack modes for Python

## What it does
Two standalone scripts that attempt to crack the password of a password-protected ZIP file. `bruteforce.py` generates all alphanumeric combinations up to length 4; `dictionaryattack.py` tests passwords from user-supplied wordlists plus keyword combinations.

## Features
- **Brute force**: tries all alphanumeric combinations (a–z, A–Z, 0–9) up to length 4
- **Dictionary attack**: loads up to 3 custom wordlist `.txt` files plus user-defined keywords
- Keyword combination mode — generates pairwise combos of provided keywords
- Live progress counter for each attempt

## Requirements
```
Python 3.x — no third-party packages (stdlib only)
```

## Usage

**Brute force:**
1. Place your ZIP file in the same directory
2. Edit `bruteforce.py`: set `filename` and the internal file name in `z.extract()`
3. Run: `python bruteforce.py`

**Dictionary attack:**
1. Edit `dictionaryattack.py`: set `filename`, add hints to `keywords = []`, provide wordlist `.txt` files
2. Run: `python dictionaryattack.py`

## Security note
For **authorized use only** — recovering your own forgotten ZIP password, CTF challenges, or security research. Do not use on files you do not own.

## License
MIT
