from telebot import TeleBot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
import threading
import time

def get_week_keyboard():
    markup = InlineKeyboardMarkup()
    markup.row(
        InlineKeyboardButton("Четная неделя", callback_data="even_week"),
        InlineKeyboardButton("Нечетная неделя", callback_data="odd_week")
    )
    return markup

def get_back_keyboard():
    markup = InlineKeyboardMarkup()
    markup.row(InlineKeyboardButton("Вернуться в меню", callback_data="back_to_menu"))
    return markup

def get_even_day_keyboard():
    markup = InlineKeyboardMarkup()
    markup.row(InlineKeyboardButton("Понедельник", callback_data="even_week_monday"))
    markup.row(InlineKeyboardButton("Вторник", callback_data="even_week_tuesday"))
    markup.row(InlineKeyboardButton("Среда", callback_data="even_week_wednesday"))
    markup.row(InlineKeyboardButton("Четверг", callback_data="even_week_thursday"))
    markup.row(InlineKeyboardButton("Пятница", callback_data="even_week_friday"))
    markup.row(InlineKeyboardButton("Суббота", callback_data="even_week_saturday"))
    markup.row(InlineKeyboardButton("Вернуться в меню", callback_data="back_to_menu"))
    return markup

def get_odd_day_keyboard():
    markup = InlineKeyboardMarkup()
    markup.row(InlineKeyboardButton("Понедельник", callback_data="odd_week_monday"))
    markup.row(InlineKeyboardButton("Вторник", callback_data="odd_week_tuesday"))
    markup.row(InlineKeyboardButton("Среда", callback_data="odd_week_wednesday"))
    markup.row(InlineKeyboardButton("Четверг", callback_data="odd_week_thursday"))
    markup.row(InlineKeyboardButton("Пятница", callback_data="odd_week_friday"))
    markup.row(InlineKeyboardButton("Суббота", callback_data="odd_week_saturday"))
    markup.row(InlineKeyboardButton("Вернуться в меню", callback_data="back_to_menu"))
    return markup
def get_back_even_keyboard():
    markup = InlineKeyboardMarkup()
    markup.row(InlineKeyboardButton("Вернуться к выбору дня", callback_data="even_week"))
    return markup
def get_back_odd_keyboard():
    markup = InlineKeyboardMarkup()
    markup.row(InlineKeyboardButton("Вернуться к выбору дня", callback_data="odd_week"))
    return markup