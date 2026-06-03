import ciphers.caesar as caesar

def encrypt_command(args):
    print(caesar.encrypt(args.text, args.shift))

def decrypt_command(args):
    print(caesar.decrypt(args.text, args.shift))
