import random

# For now, we return a random roast (1 roast per request)
ROASTS = [
    "Even your username gave up halfway.",
    "This name sounds like your WiFi password.",
    "You're one vowel away from total disaster.",
    "I've seen captchas with more brand appeal.",
    "No one's minting this unless they lost a bet.",
    "This belongs in the username graveyard.",
    "You typed that and still hit send?",
    "I’d pay to never see this username again.",
    "Congrats, you just broke the ugly limit.",
    "Usernames have feelings too, and you hurt them."
]

def handle_roast_command(update, context):
    if not context.args:
        update.message.reply_text("Send a username to roast. Usage: `.roast @username`")
        return

    username = context.args[0].lstrip("@").lower()
    burn = random.choice(ROASTS)
    update.message.reply_text(f"@{username} – {burn}")

