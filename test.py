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