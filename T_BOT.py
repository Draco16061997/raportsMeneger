from aiogram import Bot, Dispatcher, types, executor
import string
import random

Token ='5854629919:AAH4LU9HREMQ6OKbA9QgEsbGaSShiKJ2ZWY'

bot = Bot(Token)
dp = Dispatcher(bot)
async def on_startup(_):
    print("BOT STARTED!")

@dp.message_handler(commands = ['start'])
async def start_command(message: types.Message):
    await message.answer('Hello man')
    print('New User')
    print(f'ID_USER: {message["from"]["id"]}')
    print(f'{message["from"]["first_name"]} {message["from"]["last_name"]}')

    print(f'@{message["from"]["username"]}')
    print(message)



@dp.message_handler(commands = ['help'])
async def help_command(message: types.Message):
    await message.reply('12123')

# @dp.message_handler()
# async def upper_echo(message: types.Message):
#     await message.answer(message.text.upper())

# @dp.message_handler()
# async def upper_echo(message: types.Message):
#     if message.text.count(' ')>=1
#         await message.answer(message.text)
#         # await message.delete() delete messege
coun = 0
@dp.message_handler(commands = ['count'])
async def count(message: types.Message):
    global coun
    await message.answer(f'COUNT {coun}')
    print(message)
    coun += 1

@dp.message_handler()
async def random_leather(message: types.Message):
    await message.answer(random.choice(string.ascii_letters))
    print(message)

if __name__ =='__main__':
    executor.start_polling(dp, on_startup=on_startup)

