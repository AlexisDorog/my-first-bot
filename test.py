# # дебильный калькулятор v1
# from colorama import init
# from colorama import Fore, Back, Style
#
# init()
# print(Fore.BLACK)
# print(Back.GREEN)
#
# what = input('Что делаем? (+, -):')
#
# print(Back.CYAN)
#
# a = float(input('Введи первое число: '))
#
# b = float(input('Введи второе число: '))
# print(Back.LIGHTRED_EX)
#
# if what == '+':
#     c = str(a + b)
#     print('Результат: ' + c)
# elif what == '-':
#     c = str(a + b)
#     print('Результат: ' + c)
# else:
#     print('Выбрана неверная операция')
#
# import pyowm
# owm = pyowm.OWM('b1d762c98307645904235b33b197a86a')
# mgr = owm.weather_manager()
#
# place = input('В каком городе,стране нужна погода?:')
#
# observation = mgr.weather_at_place(place)
# w = observation.weather
# if w.detailed_status == 'rain':
#     print('На улице rain - на душе pain')
# else:
#     print("В городе "+ place + " сейчас "+ w.detailed_status )
#
# temp = w.temperature('celsius')['temp']
# print("На улице "+ str(temp) +" градусов")
#
# if temp < 10:
#     print("Выпей водки перед выходом на улицу!")
# elif temp < 20:
#     print("Согреться пивом будет достаточно.")
# else:
#     print('Можно идти в трусах - на улице жара.')
# # print(w)
import pyowm
import telebot

owm = pyowm.OWM('b1d762c98307645904235b33b197a86a')
bot = telebot.TeleBot("5403430121:AAF3CHmGDHzz0orWKXZQxS-At5Ch-K4xSwU", parse_mode=None)
mgr = owm.weather_manager()

@bot.message_handler(content_types=['text'])
def send_echo(message):
	observation = mgr.weather_at_place(message.text)
	w = observation.weather
	if w.detailed_status == 'rain':
	    answer = "На улице rain - на душе pain" + '\n'
	else:
	    answer = "В городе "+ message.text + " сейчас "+ w.detailed_status + '\n'

	temp = w.temperature('celsius')['temp']
	answer += "На улице "+ str(temp) +" градусов" + '\n\n'

	if temp < 10:
	    answer +="Выпей водки перед выходом на улицу!"
	elif temp < 20:
	    answer +="Согреться пивом будет достаточно."
	else:
	    answer +='Можно идти в трусах - на улице жара.'
	# bot.reply_to(message, message.text)
	bot.send_message(message.chat.id, answer)
bot.polling(none_stop = True)