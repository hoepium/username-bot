from username_utils import classify_username, estimate_username_value
from image_generator import generate_pricing_image
from telegram import InputMediaPhoto
import io

def handle_rate_command(update, context):
    if not context.args:
        update.message.reply_text("Please provide a username. Usage: `.rate @username`")
        return

    raw_username = context.args[0]
    username = raw_username.lstrip("@").lower()

    # Step 1: Classify username
    category, details = classify_username(username)

    # Step 2: Estimate price and generate pros/cons
    price, comments = estimate_username_value(username, category, details)

    # Step 3: Generate image with gradient + price
    image_bytes = generate_pricing_image(username, price, comments)

    # Step 4: Send the image back
    update.message.reply_photo(
        photo=io.BytesIO(image_bytes),
        caption=f"Evaluation for @{username}",
        filename=f"{username}.png"
    )
