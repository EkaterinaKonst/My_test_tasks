import requests
from bs4 import BeautifulSoup
import os
import telebot

url = 'https://vc.ru/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
all_title = soup.find_all("div", class_="content-container")
last_news = all_title[0].text


TOKEN = os.getenv("TOKEN")
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(content_types=['text'])
def send_new(message):

    if message.text.lower() == "Привет":
        text = last_news
        bot.send_message(message.from_user.id, text)
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Для получения последней новости с vc.ru напиши 'Привет'")
    else:
        bot.send_message(message.from_user.id, "Для получения справки напиши /help.")


if __name__ == '__main__':
    bot.polling(none_stop=True, interval=0)