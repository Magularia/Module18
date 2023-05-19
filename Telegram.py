# import telebot
#
# TOKEN = "6100688302:AAF4bZ8gp4cZ0VnIAdfG4xXNBtKokzoRRCE"
#
# bot = telebot.TeleBot(TOKEN)
#
#
# # Обрабатываются все документы и аудиозаписи
# # @bot.message_handler(content_types=['document', 'audio'])
# # def handle_docs_audio(message):
# #     pass
# @bot.message_handler(commands=['start', 'help'])
# def send_welcome(message):
#     bot.send_message(message.chat.id, f"Привет, {message.chat.username}")
#
# @bot.message_handler(content_types=['voice'])
# def repeat(message: telebot.types.Message):
#     bot.send_message(message.chat.id, "У тебя красивый голос")
#
# @bot.message_handler(content_types=['photo', ])
# def say_lmao(message: telebot.types.Message):
#     bot.reply_to(message, 'Nice meme XDD')
#
# bot.polling(none_stop=True)