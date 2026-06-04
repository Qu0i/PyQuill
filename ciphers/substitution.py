from utility.mapping import build_mapping

def transform(text: str, source_alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ", target_alphabet="ZYXWVUTSRQPONMLKJIHGFEDCBA") -> str:
    result = ""
    mapping = build_mapping(source_alphabet, target_alphabet)

    for char in text:
        if char.isalpha():
            is_lower = char.islower()
            char = char.upper()

            mapped = mapping[char]

            result += mapped.lower() if is_lower else mapped
        else:
            result += char

    return result