# username_utils.py

# username_utils.py

import re
import enchant

dictionary = enchant.Dict("en_US")

def is_real_word(username: str) -> bool:
    """Checks if the username is a valid English word."""
    return dictionary.check(username.lower())

def is_four_char(username: str) -> bool:
    """Returns True if username is exactly 4 characters."""
    return len(username) == 4

def is_mixed_or_numeric(username: str) -> bool:
    """Returns True if username has numbers or mix of letters and numbers."""
    return bool(re.search(r'\d', username))

def is_aesthetic_negative_word(username: str) -> bool:
    """Detects aesthetic, nihilistic or negative-tone words like 'hopeless'."""
    negative_suffixes = ['less', 'void', 'fail', 'doom', 'lost']
    return (
        is_real_word(username)
        and any(username.lower().endswith(suffix) for suffix in negative_suffixes)
        and not has_commercial_use(username)
    )

def has_commercial_use(username: str) -> bool:
    """Rough logic to detect if real word is commonly used in business/branding."""
    commercial_keywords = ['shop', 'pay', 'market', 'cloud', 'app', 'tech', 'coin']
    return any(word in username.lower() for word in commercial_keywords)

def categorize_username(username: str) -> str:
    """
    Categorizes username into:
    - premium
    - real_word
    - aesthetic_negative
    - brandable
    - four_char
    - mixed_numeric
    - low_value
    """
    uname = username.lower()

    if is_four_char(uname):
        return 'four_char'
    elif is_real_word(uname):
        if has_commercial_use(uname):
            return 'premium'
        elif is_aesthetic_negative_word(uname):
            return 'aesthetic_negative'
        else:
            return 'real_word'
    elif is_mixed_or_numeric(uname):
        return 'mixed_numeric'
    elif len(uname) >= 6 and uname.endswith(('ive', 'less', 'ly', 'ed', 'ous')):
        return 'brandable'
    else:
        return 'low_value'
