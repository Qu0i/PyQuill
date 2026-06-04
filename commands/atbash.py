from ciphers import substitution

def atbash_command(args):
    print(substitution.transform(args.text))
