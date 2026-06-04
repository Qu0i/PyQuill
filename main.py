import argparse
import commands.caesar as caesar_commands

import commands.substitution as substitution_commands
import commands.atbash as atbash_commands

parser = argparse.ArgumentParser(prog="PyQuill", description="Simple command-line cipher tool.")

ciphers = parser.add_subparsers(dest="cipher")

atbash = ciphers.add_parser("atbash")
atbash_action = atbash.add_subparsers(dest="action")

atbash_transform_parser = atbash_action.add_parser("transform")
atbash.add_argument("text")
atbash.set_defaults(func=atbash_commands.atbash_command)

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

substitution = ciphers.add_parser("substitution")
substitution_actions = substitution.add_subparsers(dest="action")

transform_parser = substitution_actions.add_parser("transform")
transform_parser.add_argument("text")
transform_parser.add_argument("--source-alphabet", default="ABCDEFGHIJKLMNOPQRSTUVWXYZ", type=str)
transform_parser.add_argument("--target-alphabet", default="ZYXWVUTSRQPONMLKJIHGFEDCBA", type=str)
transform_parser.set_defaults(func=substitution_commands.substitution_command)

def main():
    args = parser.parse_args()

    args.func(args)

if __name__ == "__main__":
    main()
