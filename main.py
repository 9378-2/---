import telebot
import os

TOKEN = os.environ.get("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, "Нетидинахуй")

@bot.message_handler(func=lambda m: True)
def ifno(message):
    if not message.text:
        return

    text = message.text.lower()

    if text == "привет":
        bot.send_message(message.chat.id, "Нетидинахуй")
    elif "савелий" in text:
        bot.send_message(message.chat.id, "савелий сын шлюхи")
    elif "корнет" in text:
        bot.send_message(message.chat.id, "корнет —  нищета ебанная живущая в окопе")
    elif "кета" in text:
        bot.reply_to(message, "Омнiмэн")
    elif "схуяли" in text or "почему" in text:
        bot.reply_to(message, "Всевышний мзбб, творец всего так захотел")
    elif "ангина" in text or "ванесса" in text:
        bot.reply_to(message, "Ангина любит сосать (хуи)")

bot.delete_webhook()
bot.polling(none_stop=True)
