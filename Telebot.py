import telebot
from telebot import types
from extensions import CurrencyConverter, APIException
from Config import TOKEN

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_instructions(message):
    instructions = "Добро пожаловать, это бот для конвертации валют!\n\nДля того чтобы узнать цену на валюту , пожалуйста введите: <имя_валюты_для_конверта> <имя_другой_валюты> <сумма>\nДля примера: EUR USD 100"
    bot.send_message(message.chat.id, instructions)

@bot.message_handler(commands=['values'])
def send_available_currencies(message):
    available_currencies = "Доступные валюты:\nEuro - EUR\nUS Dollar - USD\nRussian Ruble - RUB"
    bot.send_message(message.chat.id, available_currencies)

@bot.message_handler(func=lambda message: True)
def convert_currency(message):
    try:
        currency_from, currency_to, amount = message.text.split()
        amount = float(amount)
        result = CurrencyConverter.get_price(currency_from.upper(), currency_to.upper(), amount)
        bot.send_message(message.chat.id, f"The price of {amount} {currency_from.upper()} in {currency_to.upper()} is {result}")
    except ValueError:
        bot.send_message(message.chat.id, "Пожалуйста, введите название валюты, названия другой валюты, и сумма, разделенные пробелами.")
    except APIException as e:
        bot.send_message(message.chat.id, f"Error: {str(e)}")

bot.polling()