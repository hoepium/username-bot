import re
from username_utils import (
    is_real_word,
    is_4_letter,
    is_negative_tone,
    has_fragment_sale,
    is_brandable
)
from image_generator import generate_image

def handle_rate_command(username: str):
    username_clean = username.strip().lower().replace("@", "")
    errors = []

    # Basic username rules
    if len(username_clean) < 4:
        errors.append("❌ Username too short. Telegram requires 4+ characters.")
    if not re.match("^[a-z0-9_]+$", username_clean):
        errors.append("❌ Username must only contain letters, numbers, or underscores.")
    if "__" in username_clean or username_clean.startswith("_") or username_clean.endswith("_"):
        errors.append("❌ Avoid starting/ending with or repeating underscores.")

    # Fragment rule: only all-letter 4-character usernames exist
    if len(username_clean) == 4 and not username_clean.isalpha():
        errors.append("❌ 4-character usernames must be all letters (no numbers or symbols).")
    
    if errors:
        return "\n".join(errors), None

    # Now determine price logic
    info = []
    price = 0
    category = "other"

    # Check for 4-letter (strict Fragment pricing)
    if is_4_letter(username_clean):
        category = "4-letter"
        info.append("🔐 4-letter exclusive Telegram username.")
        info.append("🏷️ Priced using Fragment's floor: 5050 TON ($16,616).")
        price = 16616

    # Real dictionary word logic
    elif is_real_word(username_clean):
        category = "real_word"
        if is_negative_tone(username_clean):
            info.append("🌀 Aesthetic, negative-tone real word.")
            price = 120  # Midpoint of 80–150
        else:
            info.append("📘 Recognized real word.")
            price = 600  # Mid of 400–800 range
            if has_fragment_sale(username_clean):
                info.append("💎 This word has past Fragment sale history.")
                price = 850  # Raise to premium
            elif username_clean in {"playboy", "fame", "divine", "envy", "hype"}:
                info.append("🔥 High cultural relevance detected.")
                price = 1000

    # Brandable, clean coined usernames
    elif is_brandable(username_clean):
        category = "brandable"
        info.append("🧠 Clean, brandable name (not real word).")
        price = 70  # Mid of $50–90 range

    # Mid-quality coined or odd usernames
    else:
        info.append("🪐 Coined or niche name. No strong brand/culture signal.")
        price = 25  # Conservative floor
        category = "coined"

    info.append(f"💰 Estimated Market Value: ${price:,}")
    image = generate_image(username_clean, price, "\n".join(info), category)
    return "\n".join(info), image
