# 🇫🇷 French-to-Voice Telegram Bot

A Telegram bot that takes a French text input and converts it into speech (audio) using Google Text-to-Speech (gTTS). The bot also provides an English translation of the French text.

## 🚀 Features

- 🎤 Convert French text into speech (audio) and send it back as a voice message.
- 🌍 Translate the French text to English and provide the translation as a caption in the voice message.
- 🤖 Powered by the Telegram Bot API and Google services (gTTS & Google Translate).
- 💬 Simple interaction via Telegram: send French text, receive audio and translation.

## 🛠 Requirements

- Python 3.8+
- Telegram bot token
- Google Translate API
- Google Text-to-Speech (gTTS) library

Install dependencies:

```bash
pip install -r requirements.txt
```

## 🔐 Environment Variables
Create a .env file in the root directory with the following values:
```
bot_api_key=YOUR_BOT_TOKEN
```
Replace YOUR_BOT_TOKEN with your actual Telegram bot token, which you can get by creating a bot via @BotFather.


## ▶️ Running the Bot
Start the bot with:
```
python run.py
```
Once running, you can interact with the bot by sending French text, and it will respond with the audio and English translation.

### 📦 run.py
Contains the main bot logic:

Translates French text into English.

Converts French text to speech using gTTS.

Sends the audio file and the translation as a message in Telegram.

### 📜 Text to Speech Feature
The bot takes French text, converts it to speech using Google's Text-to-Speech (gTTS) service, and sends it back as a voice message.

###  🗣 Translation
The bot uses the googletrans library to translate French text into English, which is then added as a caption in the voice message.


## ⚠️ Disclaimer
- This bot is intended for educational and personal use only.
- Ensure compliance with Google’s [Terms of Service](https://cloud.google.com/terms).
- This bot uses the Google Translate API and gTTS for translation and speech generation.


## 🤝 Contributing

Contributions are welcome!  
If you have ideas, bug fixes, or improvements, feel free to fork the repo and open a pull request.

For major changes, please open an issue first to discuss the proposed changes.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/my-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/my-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License.  
See the [LICENSE](LICENSE) file for details.

&copy; [Ilia Abolhasani](https://github.com/Ilia-Abolhasani)
