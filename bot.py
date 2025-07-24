import os
import asyncio
from pyrogram import Client, filters
from rate_logic import analyze_username
from roast_logic import roast_username

API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Client("username_eval_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@bot.on_message(filters.command("start"))
async def start(_, msg):
    await msg.reply(
        "**👋 Welcome to the Telegram Username Evaluator Bot!**\n\n"
        "This bot gives you clean, AI-generated evaluations for Telegram usernames using smart branding logic, aesthetics, and sale history from platforms like Fragment.\n\n"
        "**Available Commands:**\n"
        "- `.rate @username` – Honest AI-powered username review with price estimation and image.\n"
        "- `.roast @username` – Sarcastic, text-only roast (one-time unique burn per user).\n\n"
        "> ⚠️ **Disclaimer:**\n"
        "This bot is an AI-based tool. While it considers Fragment sales and branding logic, the estimated prices may not always reflect the real market value. Always do your own research before buying or selling usernames."
    )

@bot.on_message(filters.command("rate", prefixes=".") & filters.me)
async def rate_handler(_, msg):
    if len(msg.command) < 2:
        await msg.reply("Please provide a username to rate.\nUsage: `.rate @username`")
        return

    username = msg.command[1]
    await msg.reply("Analyzing username...")

    try:
        result = analyze_username(username)
        image_path = result["image_path"]
        caption = (
            f"**@{username.lower().strip('@')}**\n"
            f"Estimated Price: `${result['price']:,}`\n"
            f"Category: {result['category']}\n"
            f"{result['notes']}"
        )
        await msg.reply_photo(photo=image_path, caption=caption)
    except Exception as e:
        await msg.reply(f"Error generating result: {e}")

@bot.on_message(filters.command("roast", prefixes=".") & filters.me)
async def roast_handler(_, msg):
    if len(msg.command) < 2:
        await msg.reply("Please provide a username to roast.\nUsage: `.roast @username`")
        return

    username = msg.command[1]
    roast = roast_username(username)
    await msg.reply(roast)

if __name__ == "__main__":
    bot.run()
