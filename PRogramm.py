
import telebot
from telebot import types
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

bot = telebot.TeleBot('1157810407:AAHwvYtta12trNgT2hXUq9HtzdAuYU05JzI');


@bot.message_handler(commands=['start'])
def start(message):
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	btn2 = types.KeyboardButton(" Задать вопрос")
	markup.add(btn2)
	bot.send_message(message.chat.id, text="Привет, {0.first_name}! Я бот поддержки, Нажми на кнопку и можешь задавать свой вопрос  ".format(message.from_user), reply_markup=markup)



r1 = 0
@bot.message_handler(content_types=['text'])
def get_text_id(message):
	global r1


	def spec_text(message):
		bot.send_message(5454762659, message.text)

	def texts(message):
		global r1

		text_nash = 'Расписание'
		com = fuzz.ratio(message.text, text_nash)
		print(com)

		if com >= 40:
			markup = types.InlineKeyboardMarkup()
			button1 = types.InlineKeyboardButton("Календарь GeekBrains ", url='https://gb.ru/calendar')
			markup.add(button1)
			bot.send_message(message.chat.id, "Ты можеш получить ответ здесь:".format(message.from_user), reply_markup=markup)

			print("Вопрос ",message.text)
		elif com < 40:
			global r1

			
			if r1 == 1:
				bot.send_message(message.from_user.id, "Перевёл ваш вопрос на специалиста")

				markup1 = types.InlineKeyboardMarkup()
				button11 = types.InlineKeyboardButton("Ответить ", url='https://gb.ru/calendar')
				markup1.add(button11)

				bot.send_message(5454762659, message.text, reply_markup=markup1)
				print('id пользователя', message.chat.id)
				r1 = 0
			else:
				markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
				btn2 = types.KeyboardButton(" Задать вопрос")
				markup.add(btn2)
				bot.send_message(message.chat.id, text="Я вас не понимаю перефрозируйте пожалуйста свой вопрос".format(message.from_user), reply_markup=markup)
				r1 = r1 + 1

			

	if message.text == "Задать вопрос":
		a = bot.send_message( message.from_user.id, "Слушаю")
		b = bot.register_next_step_handler(a, texts)
		print(123)
		
	else:
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
		btn2 = types.KeyboardButton(" Задать вопрос")
		markup.add(btn2)

		bot.send_message(message.from_user.id, "Перед тем как задавать вопрос нажмите на кнопку".format(message.from_user), reply_markup=markup)
	
	




bot.polling(none_stop=True, interval=0)
