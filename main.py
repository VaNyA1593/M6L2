import telebot
from config import token
from logic import generate_image

bot = telebot.TeleBot(token)

# Handle '/start' and '/help'
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Hello! I am a bot that generates images from text. /generate <prompt> to generate an image from text.")

@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.send_message(message.chat.id, "/generate <prompt> to generate an image from text.")

@bot.message_handler(commands=['generate'])
def image(message):
        raw_prompt = message.text.split(' ')
        prompt = ' '.join(raw_prompt[1:])
        generation_message = bot.send_message(message.chat.id, f"Generating {prompt}...")
        bot.send_chat_action(message.chat.id, 'typing')
        generate_image(prompt)
        bot.send_photo(message.chat.id, open('output_image.jpg', 'rb'))
        bot.send_message(message.chat.id, f"{prompt.capitalize()} generated successfully!")
        bot.delete_message(message.chat.id, generation_message.message_id)
        
bot.infinity_polling()