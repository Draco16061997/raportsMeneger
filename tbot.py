import telebot
import config
import telebot
import pyqrcode
import io
import openai
import AutocreateReport

# Замените 'YOUR_API_TOKEN' на токен вашего бота, полученный от BotFather в Telegram
API_TOKEN = config.tok

# Инициализация бота
bot = telebot.TeleBot(API_TOKEN)

user_states = {}

# Состояния
class State:
    WAITING_TEXT = 1
    GENERATING_QR = 2

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def start(message):
    print(message)
    bot.send_message(message.chat.id, "Привет! Я бот. Как я могу вам помочь?")

@bot.message_handler(commands=['QR'])
def generate_qr_command(message):
    user_id = message.chat.id
    bot.send_message(user_id, "Отправь мне текст, для которого нужно создать QR-код.")
    user_states[user_id] = State.WAITING_TEXT

# Обработчик текстовых сообщений
@bot.message_handler(func=lambda message: message.chat.id in user_states and user_states[message.chat.id] == State.WAITING_TEXT)
def process_text(message):
    user_id = message.chat.id
    text = message.text
    qr_image = generate_qr_code(text)

    # Отправка изображения QR-кода пользователю
    with open(qr_image, 'rb') as qr_image_file:
        bot.send_photo(user_id, qr_image_file, )

    # Убираем пользователя из режима ожидания текста
    del user_states[user_id]

# Функция для создания QR-кода

def generate_qr_code(text):
    qr = pyqrcode.create(text)
    # Создание изображения QR-кода в формате PNG
    qr.png('qrcode.png', scale=20)
    return 'qrcode.png'

# @bot.message_handler(commands="R")
# def getRaport(message):
#     AutocreateReport.с.createReportIsTime(AutocreateReport.d, AutocreateReport.period_to_now())



if __name__ == "__main__":
    bot.polling(none_stop=True, skip_pending=True)
