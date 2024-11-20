import logging
import crud_functions as cr
from dotenv import load_dotenv
import os
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import re
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
button_b = KeyboardButton(text='Купить')
button_reg = KeyboardButton(text='Регистрация')

kb.row(button_r,button_i)
kb.row(button_b, button_reg)


kb_i = InlineKeyboardMarkup()
butt_i_r = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
butt_i_i = InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')
kb_i.add(butt_i_r)
kb_i.add(butt_i_i)

# инлайн клавиатура для продаж кнопки заполняются в функции get_buying_list
catalog_kb = InlineKeyboardMarkup()


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

class RegistrationState(StatesGroup):
    username = State()
    email = State()
    age = State()
    balance = 1000

@dp.message_handler(text='Рассчитать')
async def main_menu(message):
    await message.answer("Выберите опцию:", reply_markup = kb_i)

@dp.message_handler(text='Купить')
async def get_buying_list(message):
    cr.initiate_db()
    products = cr.get_all_products()
    #cr.close_base()
    for item in products:
        await message.answer(f'Название {item[1]} | Описание : {item[2]} | Цена: {item[3]} ')
        catalog_kb.add(InlineKeyboardButton(text=item[1], callback_data='product_buying'))
        with open(f'img/{item[1]}.webp', 'rb') as img:
            await message.answer_photo(img, '')
    await message.answer("Выберите продукт для покупки:", reply_markup=catalog_kb)


@dp.callback_query_handler(text='product_buying')
async def send_confirm_message(call):
    await call.message.answer(f"Вы успешно приобрели {call.message.text}!")
    await call.answer()

#Регистрация
@dp.message_handler(text='Регистрация')
async def sign_up(message):
    await message.answer("Введите имя пользователя (только латинский алфавит):")
    await RegistrationState.username.set()


@dp.message_handler(state = RegistrationState.username)
async def set_username(message, state):
    is_in_base = cr.is_included(message.text)

    if not re.search(r'[^a-zA-Z0-9]', message.text) and not is_in_base:
        await state.update_data(username=message.text)
        await message.answer("Введите email:")
        await RegistrationState.email.set()
    else:
        if is_in_base:
            text = "Такой пользователь уже есть в базе"
        else:
            text = 'Имя содержит недопустимые символы'
        await message.answer(f"{text}\n/startВведите имя пользователя (только латинский алфавит):")
        await RegistrationState.username.set()

@dp.message_handler(state = RegistrationState.email)
async def set_email(message, state):
    if re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', message.text):
        await state.update_data(email=message.text)
        await message.answer("Введите свой возраст:")
        await RegistrationState.age.set()
    else:
        await message.answer("Не верный email\nВведите email:")
        await RegistrationState.email.set()

@dp.message_handler(state = RegistrationState.age)
async def set_age_r(message, state):
    if message.text.isnumeric():

        await state.update_data(age=message.text)
        data = await state.get_data()
        cr.set_users( data['username'], data['email'], data['age'])
        await message.answer("Регистрация завершена")
        await state.finish()
    else:
        await message.answer("Возраст должен быть целым числом\nВведите свой возраст:")
        await RegistrationState.age.set()


@dp.callback_query_handler(text='formulas')
async def set_formulas(call):
    await call.message.answer('Норма калорий по формуле Миффлина - Сан Жеора\n для мужчин: 10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5\nдля женщин: 10 x вес (кг) + 6,25 x рост (см) – 5 x возраст (г) – 161')
    await call.answer()

@dp.callback_query_handler(text='calories')
async def set_age(call):
    await call.message.answer("Введите свой возраст:")
    await UserState.age.set()
    await call.answer()

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
    await message.answer('Здесь вы можете приобрести товары для снижения веса!')

@dp.message_handler(commands=['start'])
async def start_message(message):
    await message.answer("Привет!  Я бот помогающий твоему здоровью.", reply_markup = kb)


@dp.message_handler()
async def all_message(message):
    await message.answer("Введите команду /start, чтобы начать общение.")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
