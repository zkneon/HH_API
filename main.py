from pprint import pprint
from telebot import TeleBot
from dotenv import load_dotenv
from os import environ
from HH_Use.hh_use import HH_Use


def main():
    load_dotenv()
    bot = TeleBot(environ.get('TOKEN'))

    @bot.message_handler(commands=['start'])
    def start_message(message):
        bot.send_message(message.chat.id, 'Hello')

    @bot.message_handler(content_types='text')
    def search_text(message):
        bot.send_message(message.chat.id, f'Start searching vacancy with context {message.text}')
        pprint(message.text)
        hh_o = HH_Use(message.text)
        hh_o.separ()
        new_vac = hh_o.get_vacancy_by_id()
        for key, item in new_vac.items():

            bot.send_message(message.chat.id, f'{item[0]}: {item[1]}')

    bot.infinity_polling()


if __name__ == '__main__':
    main()
