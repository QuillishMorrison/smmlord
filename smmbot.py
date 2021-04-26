
import telebot
joinedFile = open('C:\\Users\\Quillish Wammy\\Desktop\\botuser.txt', 'r')
joinedUsers = set()
for line in joinedFile:
	joinedUsers.add(line.strip())
joinedFile.close()

bot = telebot.TeleBot("1743253979:AAGpV8PbQrR3p1dxJtDLYarKScHJykphJmQ")


@bot.message_handler(commands=['special'])
def mess(message):
	for user in joinedUsers:
		bot.send_message(user, message.text[message.text.find(' '):])

@bot.message_handler(commands=['start', 'go'])
def send_welcome(message):
	bot.reply_to(message, "Приветствую, ты успешно зарегистрировался на мой Мастер-Класс, который состоится 10 Мая в 19:00.😉\nСсылку на онлайн мероприятие получишь за час до начала.👌\nКстати, вот твой подарок 😌")
	f = open("C:\\Users\\Quillish Wammy\\Desktop\\Документ Microsoft Word.docx", "rb")
	bot.send_document(message.chat.id,f)
	if not str(message.chat.id) in joinedUsers:
		joinedFile = open('C:\\Users\\Quillish Wammy\\Desktop\\botuser.txt', 'a')
		joinedFile.write(str(message.chat.id) + "\n")
		joinedUsers.add(message.chat.id)


@bot.message_handler(commands=['help'])
def send_welcome(message):
	bot.reply_to(message, "/start - запустить бота\n/when - узнать дату начала вебинара\n/link - получить ссылку на вебинар")

@bot.message_handler(commands=['when'])
def send_welcome(message):
	bot.reply_to(message, "Вебинар состоится 10 Мая в 19:00")

@bot.message_handler(commands=['link'])
def send_welcome(message):
	bot.reply_to(message, "Я пришлю тебе ссылку как только она станет доступна")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, "Введи /help для просмотра команд")



bot.infinity_polling()

