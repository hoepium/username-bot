import random

def handle_roast_command(username: str):
    username_clean = username.strip().lower().replace("@", "")
    
    if len(username_clean) < 4:
        return f"🔪 @{username_clean}? That’s not a username, that’s a typo."

    if username_clean.startswith("_") or username_clean.endswith("_") or "__" in username_clean:
        return f"💀 Underscores are not a personality, @{username_clean}."

    if username_clean.isdigit():
        return f"🔢 @{username_clean} — wow, numeric boredom at its peak."

    if username_clean.isalpha() and len(username_clean) == 4:
        return f"🧊 @{username_clean} — short, sharp, and still somehow forgettable."

    burns = [
        f"🥱 @{username_clean}? I’ve seen captchas with more personality.",
        f"📉 @{username_clean} — the username equivalent of a soft handshake.",
        f"🪦 @{username_clean} sounds like a failed startup from 2013.",
        f"🧹 @{username_clean} — just here to sweep up the scraps of creativity.",
        f"🎯 @{username_clean}? Missed the mark. Completely.",
        f"💤 @{username_clean} is what I’d name my alarm clock — because it puts me to sleep.",
        f"🤡 @{username_clean} — circus called, they want their clown back.",
        f"🪫 @{username_clean}? More like low battery in username form.",
        f"📦 @{username_clean} — basic, boxed, and best left unopened.",
        f"🚫 @{username_clean} is the kind of handle that makes people reconsider the internet.",
    ]

    return random.choice(burns)
