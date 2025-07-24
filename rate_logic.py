from username_utils import classify_username, estimate_username_value
from image_generator import generate_pricing_image
from telegram import InputMediaPhoto
import io

def handle_rate_command(update, context):
    if not context.args:
        update.message.reply_text("Please provide a username. Usage: `.rate @username`")
        return

    username = context.args[0].lstrip("@").lower()
    category = classify_username(username)
    price, comments = estimate_username_value(username, category)
    image_bytes = generate_pricing_image(username, price, comments)

    update.message.reply_photo(photo=io.BytesIO(image_bytes), caption=f"Evaluation for @{username}", filename=f"{username}.png")
