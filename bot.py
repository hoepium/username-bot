from telegram.ext import Updater, CommandHandler
from rate_logic import handle_rate_command
from roast_logic import handle_roast_command
import os

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

def start(update, context):
    welcome_message = (
        "**👋 Welcome to the Telegram Username Evaluator Bot!**\n\n"
        "This bot gives you clean, AI-generated evaluations for Telegram usernames "
        "using smart branding logic, aesthetics, and sale history from platforms like Fragment.\n\n"
        "**Available Commands:**\n"
        "- `.rate @username` – Honest AI-powered username review with price estimation and image.\n"
        "- `.roast @username` – Sarcastic, text-only roast (one-time unique burn per user).\n\n"
        "> ⚠️ **Disclaimer:**\n"
        "This bot is an AI-based tool. While it considers Fragment sales and branding logic, "
        "the estimated prices may not always reflect the real market value. Always do your own research."
    )
    context.bot.send_message(chat_id=update.effective_chat.id, text=welcome_message, parse_mode="Markdown")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("rate", handle_rate_command))
    dp.add_handler(CommandHandler("roast", handle_roast_command))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
