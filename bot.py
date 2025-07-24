import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from rate_logic import handle_rate_command
from roast_logic import handle_roast_command

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")  # Make sure this is set in your environment

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "**👋 Welcome to the Telegram Username Evaluator Bot!**\n\n"
        "This bot gives you clean, AI-generated evaluations for Telegram usernames using smart branding logic, aesthetics, and sale history from platforms like Fragment.\n\n"
        "**Available Commands:**\n"
        "- `.rate @username` – Honest AI-powered username review with price estimation and image.\n"
        "- `.roast @username` – Sarcastic, text-only roast (one-time unique burn per user).\n\n"
        "> ⚠️ **Disclaimer:**\n"
        "This bot is an AI-based tool. While it considers Fragment sales and branding logic, the estimated prices may not always reflect the real market value. Always do your own research before buying or selling usernames.",
        parse_mode='Markdown'
    )

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("rate", handle_rate_command))
    app.add_handler(CommandHandler("roast", handle_roast_command))
    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
