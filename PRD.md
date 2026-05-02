# PRD: attackpassword

## Overview
A minimal Python toolkit for recovering passwords from encrypted ZIP archives. Targeted at users who have forgotten their own ZIP password or need a tool for authorized penetration testing / CTF challenges. Two attack strategies: exhaustive brute force and wordlist-based dictionary attack.

## Goals
- Provide a working brute-force attack against password-protected ZIP files
- Provide a dictionary attack that accepts external wordlists and custom keyword hints
- Keep dependencies to Python stdlib only (zero install friction)

## Non-Goals
- GUI interface
- Multi-threaded / GPU-accelerated cracking
- Support for non-ZIP archive formats (7z, RAR, etc.)
- Network-based password attacks
- Storing or transmitting cracked passwords

## User Stories
- As a developer, I forgot the password of a ZIP I created, so I want a brute-force script that tries all short alphanumeric combinations.
- As a CTF player, I have hints about a ZIP password, so I want a dictionary tool that combines those keywords with a wordlist.
- As a security researcher, I want to demonstrate ZIP password weakness to justify stronger encryption policies.

## Tech Stack
- **Language**: Python 3.x
- **Libraries**: `zipfile` (stdlib), `itertools` (stdlib)
- **Runtime**: any OS with Python 3 installed

## Architecture
```
attackpassword/
├── bruteforce.py        # generates all alphanumeric strings up to length N, tries each
└── dictionaryattack.py  # loads wordlists + keyword combos, tries each against ZIP
```

### bruteforce.py logic
1. Define character set (alphanumeric, 62 chars)
2. Generate all strings of length 1..4 via nested list comprehension
3. For each candidate: call `zipfile.ZipFile.setpassword()` + `extract()`; success = print password

### dictionaryattack.py logic
1. Accept user-defined `keywords` list; generate all pairwise combinations via `itertools.combinations`
2. Load up to 3 plaintext wordlist files (one word per line)
3. Merge into single candidate list
4. Try each candidate against ZIP with same extract approach

## Features (detailed)

### Brute Force Attack
- **Input**: hardcoded ZIP filename, target filename inside ZIP, character set, max length
- **Process**: generate all permutations of lengths 1–N (default 4)
- **Output**: prints `Password is -- X -- after N tries!` on success
- **Acceptance criteria**: correctly extracts target file from ZIP on first matching password

### Dictionary Attack
- **Input**: ZIP filename, target filename, keywords array, up to 3 wordlist `.txt` paths
- **Process**: generate pairwise keyword combos + load wordlists, deduplicate, try each
- **Output**: prints password + try count on success
- **Acceptance criteria**: correctly extracts file when any list entry matches ZIP password

## Data / Config
- No config files — all settings are hardcoded constants at top of each script
- Users modify these constants before running:
  - `filename` — name of the ZIP file (must be in same directory)
  - Target filename inside ZIP passed to `z.extract()`
  - `keywords` list (dictionaryattack only)
  - Wordlist filenames `1.txt`, `2.txt`, `3.txt` (dictionaryattack only)

## Deployment / Run
```bash
# brute force
python bruteforce.py

# dictionary attack
python dictionaryattack.py
```
No installation needed beyond Python 3.

## Constraints & Notes
- **Legal**: Only use against files you own or have explicit written permission to test
- **Performance**: brute force at length 4 = 62^4 = ~14.7 million attempts; expect hours on slow hardware
- **Encoding**: ZIP passwords encoded as ASCII — non-ASCII passwords will not be found
- **Error handling**: bare `except: pass` swallows all errors; failed attempts are silently skipped
- **Max length**: brute force hardcoded to 4; extending requires changing the `range(4)` constant
