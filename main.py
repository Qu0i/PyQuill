import argparse
import ciphers.caesar as caesar
import commands.caesar as caesar_commands

parser = argparse.ArgumentParser(prog="PyQuill", description="Simple command-line cipher tool.")

ciphers = parser.add_subparsers(dest="cipher")

caesar = ciphers.add_parser("caesar")
caesar_actions = caesar.add_subparsers(dest="action")

encrypt_parser = caesar_actions.add_parser("encrypt")
encrypt_parser.add_argument("text")
encrypt_parser.add_argument("--shift", type=int, required=True)
encrypt_parser.set_defaults(func=caesar_commands.encrypt_command)

decrypt_parser = caesar_actions.add_parser("decrypt")
decrypt_parser.add_argument("text")
decrypt_parser.add_argument("--shift", required=True, type=int)
decrypt_parser.set_defaults(func=caesar_commands.decrypt_command)

def main():
    args = parser.parse_args()

    args.func(args)

if __name__ == "__main__":
    main()
