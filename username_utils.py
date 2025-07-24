import re

DICTIONARY_WORDS = {
    # Real sample entries for demonstration
    "hopeless", "low", "life", "france", "exhaust", "playboy", "fame", "scope", "fade", "hitlist",
    "lust", "pride", "shadow", "grace", "chaos", "drain", "vanish", "void", "scopeless", "loveless",
    "careless", "tireless", "flawless", "limitless", "restless", "useless", "aimless", "dreamless"
}

def is_four_letter(username: str) -> bool:
    return len(username) == 4 and username.isalpha()

def is_numeric_or_mixed(username: str) -> bool:
    return any(char.isdigit() for char in username)

def is_real_dictionary_word(word: str) -> bool:
    return word.lower() in DICTIONARY_WORDS

def split_into_parts(username: str):
    return re.split(r"[_\-.]", username.lower())

def detect_negative_aesthetic(word: str):
    return word.endswith("less") or word in {"hopeless", "scopeless", "loveless", "useless", "aimless", "dreamless"}

def classify_username(username: str):
    uname = username.lower().strip("@")
    
    # 4-letter usernames (strict Fragment rule)
    if is_four_letter(uname):
        return "4L", 5050

    # Real dictionary word
    if is_real_dictionary_word(uname):
        if detect_negative_aesthetic(uname):
            return "aesthetic_neg", 80
        elif uname in {"playboy", "fame", "shadow", "chaos"}:
            return "premium_dict", 1000
        else:
            return "real_dict", 500

    # Multi-part (like f_r_an_ce)
    parts = split_into_parts(uname)
    if all(is_real_dictionary_word(p) for p in parts):
        return "multi_real", 300

    # Brandable coined
    if not is_real_dictionary_word(uname) and not is_numeric_or_mixed(uname):
        return "brandable", 30

    # Numeric or mixed
    if is_numeric_or_mixed(uname):
        return "mixed_numeric", 20

    # Default fallback
    return "unknown", 10
