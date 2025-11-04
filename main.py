import requests
import telebot
from model import get_class

bot = telebot.TeleBot("7953596893:AAFIA2EX2n5lmrL4mnvepzZYaYeHYYdpemA")

@bot.message_handler(commands=["start"])
def start(message):
    bot.reply_to(message, "Привет!")

@bot.message_handler(content_types=["photo"])
def photo(message):
    file_info = bot.get_file(message.photo[-1].file_id)
    file_name = file_info.file_path.split("/")[-1]
    downoloaded_file = bot.download_file(file_info.file_path)
    with open(file_name,"wb") as new_file:
        new_file.write(downoloaded_file)
    name,score= get_class(labels_path = "./labels.txt", image_path = file_name) 
    bot.send_message(message.chat.id, f"Ваш гриб это { name} с вероятностью { int(score * 100) } %")













@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)


bot.polling()