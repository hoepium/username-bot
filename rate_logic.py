import re
from username_utils import (
    is_real_word,
    is_brandable,
    is_negative_aesthetic,
    is_pure_4_letters,
    is_fragment_4l_valid,
)
from image_generator import generate_username_image


def handle_rate_command(username: str):
    username = username.lower().strip('@')

    if not re.fullmatch(r'[a-z0-9_]{4,32}', username):
        return f"❌ Invalid username: @{username}.\nUsernames must be 4–32 characters with only letters, numbers, or underscores."

    # 4-character special rule
    if len(username) == 4:
        if not is_pure_4_letters(username) or not is_fragment_4l_valid(username):
            return f"❌ '{username}' is 4 characters, but it's either not all letters or not sold on Fragment.\nOnly pure-letter 4L usernames from Fragment are allowed."

        ton_price = 5050
        usd_price = ton_price * 3.3
        description = "4-letter pure Fragment username. Minimum floor enforced by market."
        pros = ["Pure 4L", "Fragment approved", "Premium tier"]
        cons = ["None – meets Fragment 4L rules"]

    elif is_real_word(username):
        if is_negative_aesthetic(username):
            usd_price = 80 + len(username) * 5
            description = "Real word with negative or introspective aesthetic. Niche branding potential."
            pros = ["Real English word", "Aesthetic tone"]
            cons = ["Limited commercial use"]
        else:
            usd_price = 400 + len(username) * 10
            description = "Generic real English word. Usable for branding or resale."
            pros = ["Real dictionary word", "Recognizable"]
            cons = ["Not culturally premium" if usd_price < 800 else ""]

    elif is_brandable(username):
        usd_price = 50 + len(username) * 5
        description = "Clean, coined brand-style username. Could work for projects or alt branding."
        pros = ["Clean + pronounceable", "Brandable"]
        cons = ["Not a real word", "No Fragment sale history"]

    else:
        usd_price = 5 + len(username) * 2
        description = "Basic or weak brand potential. Not a real word. May not resell well."
        pros = ["Usable"]
        cons = ["Low demand", "Not brandable", "Not a real word"]

    # Format price with commas
    price = f"${int(usd_price):,}"

    # Generate and return image
    image_bytes = generate_username_image(username, price, description)
    return image_bytes
