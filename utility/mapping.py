def build_mapping(source_alphabet: str, target_alphabet: str):
    mapping = {source_letter: target_letter for source_letter, target_letter in zip(source_alphabet, target_alphabet)}

    return mapping
