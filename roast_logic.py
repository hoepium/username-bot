# roast_logic.py

import random
from pyrogram import Client, filters
from pyrogram.types import Message

# Sample roast templates — can be expanded
ROAST_TEMPLATES = [
    "Imagine naming yourself '@{username}' 💀",
    "'{username}'? Bro that sounds like a rejected Xbox gamertag.",
    "'{username}'? That name couldn't even get a like on MySpace.",
    "The username '{username}' is the digital equivalent of soggy cereal.",
    "'{username}' walked so cringe could run.",
    "Using '@{username}' in 2025? Bold of you to assume anyone cares.",
    "Even spam bots wouldn’t pick '@{username}'.",
    "'{username}' — certified L since birth.",
    "That username made my WiFi disconnect out of embarrassment.",
    "Who hurt you into choosing '{username}'? 😭",
]

def generate_roast(username: str) -> str:
    """Select a random roast line and insert the username."""
    clean_name = username.strip().lstrip('@')
    template = random.choice(ROAST_TEMPLATES)
    return template.format(username=clean_name)

def setup_roast_handler(app: Client):
    """Register the .roast command handler with the bot app."""
    @app.on_message(filters.command("roast", prefixes=".") & filters.text)
    async def roast_handler(client: Client, message: Message):
        # Extract username
        parts = message.text.strip().split()
        if len(parts) < 2:
            await message.reply_text("😒 Usage: `.roast @username`", quote=True)
            return

        raw_username = parts[1]
        if not raw_username.startswith("@") or len(raw_username) < 3:
            await message.reply_text("❌ Invalid username. Example: `.roast @example`", quote=True)
            return

        roast_text = generate_roast(raw_username)
        await message.reply_text(roast_text, quote=True)

