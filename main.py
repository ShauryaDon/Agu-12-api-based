import asyncio
from pyrogram import Client

# Replace with your actual API credentials
bot = Client(
    "my_bot",
    api_id=123456,
    api_hash="your_api_hash",
    bot_token="your_bot_token"
)

FALLBACK_IMAGE = "https://i.tinypic.host/GNfC2.jpg"

async def safe_send_photo(chat_id, photo_url=FALLBACK_IMAGE, caption=""):
    try:
        return await bot.send_photo(chat_id=chat_id, photo=photo_url, caption=caption)
    except Exception as e:
        # fallback to text so bot doesn't break
        return await bot.send_message(chat_id=chat_id, text=f"⚠️ Could not send photo. Error: {e}\n{caption}")

@bot.on_message()
async def start(client, message):
    await safe_send_photo(
        chat_id=message.chat.id,
        caption="Welcome! ✅ Bot is working fine now."
    )

if __name__ == "__main__":
    bot.run()
