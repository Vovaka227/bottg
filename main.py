from telebot import TeleBot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
import threading
import time
from config import TOKEN
from logic import get_back_keyboard, get_even_day_keyboard, get_odd_day_keyboard, get_back_even_keyboard, get_back_odd_keyboard, get_week_keyboard


bot = TeleBot(TOKEN)


@bot.message_handler(commands=["start"])
def start_command(message):
    bot.send_message(
        message.chat.id,
        "Выберите четность недели:",
        reply_markup=get_week_keyboard()
    )


@bot.callback_query_handler(func=lambda call: True)
def callback_query_handler(call):
    if call.data in ["even_week", "odd_week", "back_to_menu", "even_week_monday", "even_week_tuesday", "even_week_wednesday", "even_week_thursday", "even_week_friday", "even_week_saturday", "odd_week_monday", "odd_week_tuesday", "odd_week_wednesday", "odd_week_thursday", "odd_week_friday", "odd_week_saturday"]:

        bot.answer_callback_query(call.id) 
        time.sleep(0.5) 
        bot.delete_message(call.message.chat.id, call.message.message_id)

        if call.data == "even_week":
            bot.send_message(
                call.message.chat.id,
                "Выберите день недели:",
                reply_markup=get_even_day_keyboard()
            )
        elif call.data == "odd_week":
            bot.send_message(
                call.message.chat.id,
                "Выберите день недели:",
                reply_markup=get_odd_day_keyboard()
            )
        elif call.data == "back_to_menu":
            bot.send_message(
                call.message.chat.id,
                "Выберите четность недели:",
                reply_markup=get_week_keyboard()
            )
        elif call.data == 'even_week_monday':
            bot.send_message(
                call.message.chat.id,
                "Расписание на понедельник:\n9.40  ЛИНАЛ  лек 5зд 301ауд.\n11.20  МАТАНАЛ  лек 5зд 421ауд.",
                reply_markup=get_back_even_keyboard()
            )
        elif call.data == "even_week_tuesday":
            bot.send_message(
                call.message.chat.id,
                "Расписание на вторник:\n8.00  ОРГ  лек 8зд 331ауд.",
                reply_markup=get_back_even_keyboard()
            )
        elif call.data == "even_week_wednesday":
            bot.send_message(
                call.message.chat.id,
                "Расписание на среду:\n8.00  ВВПД  лек 7зд 419ауд.\n9.40  ОРГ  пр 7зд 508ауд.\n11.20  ЛИНАЛ  пр 7зд 525ауд.",
                reply_markup=get_back_even_keyboard()
            )
        elif call.data == "even_week_thursday":
            bot.send_message(
                call.message.chat.id,
                "Расписание на четверг:\n9.40  ИНФА  лаба 7зд 337ауд.\n11.20  ИНФА  лаба 7зд 337ауд.\n13.30  ФИЛОСОФИЯ  пр 8зд 331ауд.\n15.10  МАТАНАЛ  пр 8зд 407ауд.",
                reply_markup=get_back_even_keyboard()
            )
        elif call.data == "even_week_friday":
            bot.send_message(
                call.message.chat.id,
                "Расписание на пятницу:\n9.40  ИН.ЯЗ  пр дистант\n11.20  ИН.ЯЗ  пр дистант\n13.30  ФИЗИКА  лаба 2зд 303ауд.\n15.10  ФИЛОСОФИЯ  лек 2зд 300ауд.\n16.50  ИСТОРИЯ  пр 2зд 505ауд.",
                reply_markup=get_back_even_keyboard()
            )
        elif call.data == "even_week_saturday":
            bot.send_message(
                call.message.chat.id,
                "Расписание на субботу:\n8.00 ФИЗРА  пр олимп\n9.40 ИСТОРИЯ  лек 2зд 300ауд.",
                reply_markup=get_back_even_keyboard()
            )
        elif call.data == "odd_week_monday":
            bot.send_message(
                call.message.chat.id,
                "Расписание на понедельник:\n11.20  МАТАНАЛ  лек 7зд 419ауд.\n13.30  ПРОГА  лаба 7зд 333ауд.\n15.10  ПРОГА  лаба 7зд 333ауд.",
                reply_markup=get_back_odd_keyboard()
            )
        elif call.data == "odd_week_tuesday":
            bot.send_message(
                call.message.chat.id,
                "Расписание на вторник:\n8.00  ФИЗРА  пр олимп\n9.40  ФИЗИКА  пр 2зд  424ауд.\n11.20  ОРГ  пр 2зд 512ауд.\n13.30  ИНФА  лек 7зд 419ауд.",
                reply_markup=get_back_odd_keyboard()
            )
        elif call.data == "odd_week_wednesday":
            bot.send_message(
                call.message.chat.id,
                "Расписание на среду:\n9.40  МААТАНАЛ  пр 7зд 337ауд.\n11.20  ЛИНАЛ  пр 7зд 339ауд.\n13.30  ПРОГА  лек 7зд 431ауд.",
                reply_markup=get_back_odd_keyboard()
            )
        elif call.data == "odd_week_thursday":
            bot.send_message(
                call.message.chat.id,
                "Расписание на четверг:\n15.10  МАТАНАЛ  пр 8зд 407ауд.\n16.50  ИСТОРИЯ  пр 2зд 312ауд.",
                reply_markup=get_back_odd_keyboard()
            )
        elif call.data == "odd_week_friday":
            bot.send_message(
                call.message.chat.id,
                "Расписание на пятницу:\n9.40  ИН.ЯЗ  пр дистант\n13.30  ИСТОРИЯ лек 2зд лек.зал№2\n15.10  ФИЛОСОФИЯ  лек 2зд 300ауд.\n16.50  ФИЗИКА  лек 2зд 312ауд.",
                reply_markup=get_back_odd_keyboard()
            )
        elif call.data == "odd_week_saturday":
            bot.send_message(
                call.message.chat.id,
                "Расписание на субботу:\n8.00 ФИЗРА  пр олимп\n20.00 ФИЗРА лек дистант",
                reply_markup=get_back_odd_keyboard()
            )

def polling():
    bot.infinity_polling()

thread = threading.Thread(target=polling)
thread.start()