import os
import sys
import telebot
from gtts import gTTS
from dotenv import load_dotenv

load_dotenv()

# Replace with your actual Telegram bot token
BOT_TOKEN = os.getenv("bot_api_key")
bot = telebot.TeleBot(BOT_TOKEN)


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
    audio_file = text_to_speech_french(french_text)
    if audio_file:
        with open(audio_file, "rb") as audio:
            bot.send_voice(message.chat.id, audio)
    bot.send_message(message.chat.id, f"{french_text}")


if __name__ == "__main__":
    bot.polling()
