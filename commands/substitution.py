from ciphers import substitution

def substitution_command(args):
    print(substitution.transform(args.text, args.source_alphabet, args.target_alphabet))
