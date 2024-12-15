import telebot
from config import api_key, secret_key, token
from logic import gen_img, client

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start_handler(message):
    bot.send_message(message.chat.id, 'Write "/generate" and your prompt here')

@bot.message_handler(commands=['generate'])
def reply_handler(message):
    bot.send_message(message.chat.id, 'Wtire your prompt here')
    bot.register_next_step_handler(message, generate_handler)

def generate_handler(message):
    bot.send_message(message.chat.id, 'Wait 1-2 minutes')
    prompt = message.text
    paht = gen_img(prompt)
    with open(paht, 'rb') as photo:
        bot.send_photo(message.chat.id, photo)



if __name__ == "__main__":
    bot.polling(none_stop=True)