import random
from decouple import config

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from config import ALARMS_ARRAY, NUCLEAR_ARRAY, SHAHED_ARRAY, BAVOVNA_ARRAY, PUSHKIN_ARRAY, BAVOVNA_IMGS, NUCLEAR_IMGS, PUSHKIN_IMGS


TOKEN_API = config('TOKEN_API')

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)


async def on_startup(_):
    print('bot is started')


@dp.message_handler(commands=['start'])
async def nuclear_bomb(message: types.Message):
    await message.answer(text=',',)
    # reply_markup=kb)
    await message.delete()


@dp.message_handler()
async def echo(message: types.Message):
    #    if 'ботов' in message.text:
    #        return await message.answer(text='согласен')

    for i in ALARMS_ARRAY:
        if i in message.text.lower():
            await bot.send_sticker(chat_id=message.chat.id,
                                   sticker='CAACAgIAAxkBAAEG0lBjmaZ5Q_wayoo_1wLcIvezvjU1AAMqGQAC3wvJSRwN8WrfLQpQLAQ')

    for i in NUCLEAR_ARRAY:
        if i in message.text.lower():
            await bot.send_photo(chat_id=message.chat.id,
                                 photo=random.choice(NUCLEAR_IMGS))

    for i in SHAHED_ARRAY:
        if i in message.text.lower():
            await bot.send_photo(chat_id=message.chat.id,
                                 photo='https://forbes.ua/static/storage/thumbs/414x671/c/8c/53a306eb-8f288b8001948dbdeb43e930822ca8cc.jpg?v=5142_3')

    for i in BAVOVNA_ARRAY:
        if i in message.text.lower():
            await bot.send_photo(chat_id=message.chat.id,
                                 photo=random.choice(BAVOVNA_IMGS))

    for i in PUSHKIN_ARRAY:
        if i in message.text.lower():
            await bot.send_photo(chat_id=message.chat.id,
                                 photo=random.choice(PUSHKIN_IMGS))

    if 'бах' in message.text.lower():
        await bot.send_photo(chat_id=message.chat.id,
                             photo='https://upload.wikimedia.org/wikipedia/commons/thumb/6/6a/Johann_Sebastian_Bach.jpg/260px-Johann_Sebastian_Bach.jpg')


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)
