import re
import os
import sys
import telebot
from gtts import gTTS
from dotenv import load_dotenv
from googletrans import Translator


translator = Translator()

load_dotenv()

# Replace with your actual Telegram bot token
BOT_TOKEN = os.getenv("bot_api_key")
bot = telebot.TeleBot(BOT_TOKEN)


def translate_to_english(text):
    try:
        translated = translator.translate(text, src="fr", dest="en")
        return translated.text
    except Exception as e:
        print(f"Translation error: {e}")
        return ""


def escape_markdown_v2(text):
    special_chars = r"\_*[]()~`>#+-=|{}.!"
    return re.sub(f"([{re.escape(special_chars)}])", r"\\\1", text)


def text_to_speech_french(text, filename="output.mp3"):
    try:
        tts = gTTS(text=text, lang="fr")  # Convert text to speech in French
        tts.save(filename)  # Save the audio file
        return filename
    except Exception as e:
        print(f"Error: {e}")
        return None


@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.reply_to(
        message,
        "Bonjour! Envoyez-moi un texte en français, et je vous enverrai l'audio.",
    )


@bot.message_handler(func=lambda message: True)
def handle_message(message):
    french_text = message.text
    english_text = translate_to_english(french_text)
    audio_file = text_to_speech_french(french_text)
    caption = f"{escape_markdown_v2(french_text)}\n\nTraduction:\n||{escape_markdown_v2(english_text)}||"
    if audio_file:
        with open(audio_file, "rb") as audio:
            bot.send_voice(
                message.chat.id, audio, caption=caption, parse_mode="MarkdownV2"
            )


if __name__ == "__main__":
    bot.polling()
