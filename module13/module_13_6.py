from dotenv import load_dotenv
import os

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import asyncio

#получаем token
load_dotenv()
api = os.getenv("API")

def norm_calories(age, growth , weight ):
    #расчёт норм калорий для мужчин
    # return 10 * float(weight) + 6.25 * float(growth) - 5 * float(age) + 5
    # расчёт норм калорий для женщин
    return 10 * float(weight) + 6.25 * float(growth) - 5 * float(age) -161


bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())
kb = ReplyKeyboardMarkup(resize_keyboard=True)
button_r = KeyboardButton(text='Рассчитать')
button_i = KeyboardButton(text='Информация')
kb.row(button_r,button_i)
kb_i = InlineKeyboardMarkup()



butt_i_r = InlineKeyboardButton(text = 'Рассчитать норму калорий' , callback_data='calories')
butt_i_i = InlineKeyboardButton(text = 'Формулы расчёта' , callback_data='formulas')
kb_i.add(butt_i_r)
kb_i.add(butt_i_i)

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()




@dp.message_handler(text='Рассчитать')
async def main_menu(message):
    await message.answer("Выберите опцию:", reply_markup = kb_i)


@dp.callback_query_handler(text='formulas')
async def set_formulas(call):
    await call.message.answer('Норма калорий по формуле Миффлина - Сан Жеора\n для мужчин: 10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5\nдля женщин: 10 x вес (кг) + 6,25 x рост (см) – 5 x возраст (г) – 161')


@dp.callback_query_handler(text='calories')
async def set_age(call):
    await call.message.answer("Введите свой возраст:")
    await UserState.age.set()



@dp.message_handler(state = UserState.age)
async def set_growth(message, state):
    await state.update_data(age1=message.text)
    await message.answer("Введите свой рост:")
    await UserState.growth.set()

@dp.message_handler(state = UserState.age)
async def set_growth(message, state):
    await state.update_data(age1=message.text)
    await message.answer("Введите свой рост:")
    await UserState.growth.set()

@dp.message_handler(state = UserState.age)
async def set_growth(message, state):
    await state.update_data(age1=message.text)
    await message.answer("Введите свой рост:")
    await UserState.growth.set()

@dp.message_handler(state = UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth1=message.text)
    await message.answer("Введите свой вес:")
    await UserState.weight.set()

@dp.message_handler(state = UserState.weight)
async def set_send_calories(message, state):
    await state.update_data(weight1=message.text)
    data = await state.get_data()
    calories =  norm_calories(data['age1'], data['growth1'],data['weight1'])
    await message.answer(f"Ваша норма калорий: {calories}")
    await state.finish()

@dp.message_handler(text='Информация')
async def inform(message):
    await message.answer('Норма калорий по формуле Миффлина - Сан Жеора\n для мужчин: 10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5\nдля женщин: 10 x вес (кг) + 6,25 x рост (см) – 5 x возраст (г) – 161')

@dp.message_handler(commands=['start'])
async def start_message(message):
    await message.answer("Привет!  Я бот помогающий твоему здоровью.", reply_markup = kb)


@dp.message_handler()
async def all_message(message):
    await message.answer("Введите команду /start, чтобы начать общение.")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)