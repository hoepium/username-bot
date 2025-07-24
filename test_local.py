from rate_logic import rate_username

if __name__ == "__main__":
    username = "hopeless"
    result = rate_username(username)
    print(f"Price: {result['price_str']}")
    print("Pros:", result['pros'])
    print("Cons:", result['cons'])

    from image_generator import generate_image
    generate_image(username, result['price_str'], result['pros'], result['cons'], save_path="preview.png")
    print("✅ Preview saved as preview.png")
