# username_utils.py

import re
import random
import json

# Load dictionary words once
with open("english_words.json", "r") as f:
    ENGLISH_WORDS = set(json.load(f))

# Helper: check if username is a real English word
def is_real_word(username: str) -> bool:
    return username.lower() in ENGLISH_WORDS

# Helper: check if it's a 4-letter username (including numbers)
def is_four_letter(username: str) -> bool:
    return len(username) == 4 and re.fullmatch(r"[a-zA-Z0-9]{4}", username) is not None

# Aesthetic, nihilistic, negative-tone words (user-defined logic)
NEGATIVE_AESTHETIC_WORDS = [
    "hopeless", "scopeless", "worthless", "heartless", "soulless", "faceless", "nameless", "pointless", "useless"
]

# Detect if username fits the "negative aesthetic" vibe
def is_negative_aesthetic(username: str) -> bool:
    return username.lower() in NEGATIVE_AESTHETIC_WORDS or username.lower().endswith("less")

# Estimate price based on your logic
def estimate_price(username: str) -> tuple:
    uname = username.lower()

    if is_four_letter(uname):
        # Fragment 4L floor
        return (16616, "4-character username (Fragment floor: 5050 TON)")

    if is_real_word(uname):
        if is_negative_aesthetic(uname):
            return (80 + random.randint(0, 70), "Real word (aesthetic negative tone)")
        elif uname in {"fame", "playboy", "exhaust"}:
            return (800 + random.randint(0, 400), "Culturally strong dictionary word")
        else:
            return (400 + random.randint(0, 400), "Real English dictionary word")

    # Brandable but not real word
    if uname.endswith("ive") or uname.endswith("ly") or uname.endswith("on") or uname.endswith("in"):
        return (50 + random.randint(0, 40), "Brandable coined username")

    # Short coined or weird usernames
    if len(uname) <= 5:
        return (20 + random.randint(0, 20), "Short coined name (not real word)")

    # Default fallback
    return (10 + random.randint(0, 15), "Low-value or random username")

# Format price nicely
def format_price(price: int) -> str:
    return f"${price:,}"

# Return a clean pros/cons summary
def get_pros_cons(username: str, price: int) -> tuple:
    uname = username.lower()
    pros = []
    cons = []

    if is_four_letter(uname):
        pros.append("Rare 4-character username")
        pros.append("Meets Fragment floor criteria (high demand)")
    elif is_real_word(uname):
        pros.append("Real English dictionary word")
        if is_negative_aesthetic(uname):
            pros.append("Aesthetic, niche branding appeal")
        else:
            pros.append("Strong commercial potential")
    else:
        pros.append("Brandable structure" if price > 50 else "Short, easy to remember")

    if not is_real_word(uname):
        cons.append("Not a real word")
    if price < 30:
        cons.append("Low resale value")
    if len(uname) > 10:
        cons.append("Too long for easy recall")

    return pros, cons
