# PyQuill

> A simple CLI tool for encrypting and decrypting text.

## Features

- [x] Caesar cipher — encrypt / decrypt


## Installation

```bash
git clone https://github.com/Qu0i/PyQuill.git
cd PyQuill
# no dependencies — pure Python
```

## Usage

```bash
# Encrypt
python main.py caesar encrypt "Hello, World!" --shift 3
# Khoor, Zruog!

# Decrypt
python main.py caesar decrypt "Khoor, Zruog!" --shift 3
# Hello, World!
```

### Subcommands

| Command | Description |
|---------|-------------|
| `caesar encrypt <text> --shift N` | Encrypt text with shift N |
| `caesar decrypt <text> --shift N` | Decrypt text with shift N |

Shift is a required `--shift` flag. Negative values and values larger than 26
wrap around correctly via modular arithmetic.

## Tests

```bash
python -m pytest -q
# ..
# 2 passed in 0.00s
```

## Project structure

```
PyQuill/
├── main.py                # Entry point, subcommand parsing
├── ciphers/               # Cipher logic
│   ├── __init__.py
│   └── caesar.py          # encrypt() / decrypt()
├── commands/              # CLI command handlers
│   ├── __init__.py
│   └── caesar.py          # encrypt_command / decrypt_command
├── tests/                 # Pytest tests
│   ├── __init__.py
│   └── test_caesar.py     # 2 tests (caesar encrypt + decrypt)
└── README.md
```

## TODO

### v 0.2
- [ ] Atbash cipher
- [ ] Vigenère cipher

### v 0.3
- [ ] File support

## License

MIT — see [LICENSE](LICENSE).
