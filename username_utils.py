import re

# ✅ Basic Oxford dictionary subset (extendable)
REAL_WORDS = {
    "fame", "hope", "ghost", "fade", "drain", "hunt", "exhaust", "playboy",
    "scope", "hopeless", "scopeless", "useless", "sadness", "panic", "dream",
    "limit", "rage", "honor", "envy", "greed", "loss", "sorrow", "numb",
    "alone", "pain", "lust", "fadeout", "fadein", "endless", "nameless",
    "weightless", "helpless", "broken", "flawless", "drain", "empty"
}

# ✅ Real negative aesthetic words
NEGATIVE_AESTHETIC = {
    "hopeless", "scopeless", "useless", "numb", "helpless", "nameless",
    "weightless", "endless", "drain", "void", "alone", "pain", "sorrow", "sadness", "empty"
}

# ✅ Check if it's a real English word
def is_real_word(username: str) -> bool:
    return username.lower() in REAL_WORDS

# ✅ Check if it's a brandable-style coined name
def is_brandable(username: str) -> bool:
    # Must be pronounceable and not purely random
    return (
        len(username) > 4
        and not is_real_word(username)
        and bool(re.fullmatch(r'[a-z]+', username))
        and any(vowel in username for vowel in "aeiou")
    )

# ✅ Check if it's one of the negative aesthetic usernames
def is_negative_aesthetic(username: str) -> bool:
    return username.lower() in NEGATIVE_AESTHETIC

# ✅ Check if it's exactly 4 characters and all letters
def is_pure_4_letters(username: str) -> bool:
    return len(username) == 4 and username.isalpha()

# ✅ Check if it's a valid 4L that matches Fragment rules (only a–z 4Ls sold)
def is_fragment_4l_valid(username: str) -> bool:
    # Fragment sold only 4-letter lowercase a–z usernames, no digits
    return username.isalpha() and len(username) == 4
