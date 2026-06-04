# PyQuill

> A simple CLI tool for encrypting and decrypting text.

## Features

- [x] Caesar cipher
- [x] Atbash cipher
 
## Installation

```bash
git clone https://github.com/Qu0i/PyQuill.git
cd PyQuill
# no dependencies — pure Python
```

## Usage

```bash
# Caesar encrypt

python main.py caesar encrypt "Hello, World!" --shift 3 # -> Khoor, Zruog!

# Caesar decrypt

python main.py caesar decrypt "Khoor, Zruog!" --shift 3 # -> Hello, World!


# Atbash

python main.py atbash transform "Hello!" # -> Svool!

# Substitution cipher

python main.py substitution transform "Hello" --source-alphabet ABCDEFGHIJKLMNOPQRSTUVWXYZ --target-alphabet MNBVCXZLKJHGFDSAPOIUYTREWQ # -> Lcggs
```

### Subcommands

| Command | Description |
|---------|-------------|
| `caesar encrypt <text> --shift N` | Encrypt text with shift N |
| `caesar decrypt <text> --shift N` | Decrypt text with shift N |
| `atbash transform <text>` | Transform text using Atbash cipher |
| `substitution transform <text> --source-alphabet ... --target-alphabet ...` | Custom substitution cipher |

`--shift` is required only for Caesar cipher. Negative values and values larger than 26
wrap around correctly via modular arithmetic.

Different ciphers may use different actions depending on their algorithm type.

## Tests

```bash
python -m pytest -q
# ..
# 3 passed in 0.00s
```

## Project structure

```
PyQuill/
├── ciphers
│   ├── __init__.py
│   ├── caesar.py
│   └── substitution.py
├── commands
│   ├── __init__.py
│   ├── atbash.py
│   ├── caesar.py
│   └── substitution.py
├── main.py
├── tests
│   ├── __init__.py
│   ├── test_caesar.py
│   └── test_substitution.py
└── utility
    └── mapping.py
```

## TODO

### v 0.2
- [x] Atbash cipher
- [x] Substitution cipher

### v 0.3
- [ ] Vigenère cipher
- [ ] File support

## License

MIT — see [LICENSE](LICENSE).
