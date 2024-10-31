from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup

import asyncio
#API_key храним в файле во избежание неприятностей
name = 'api_bot.txt'
file = open(name,'r')
api= file.read()
file.close()

def norm_calories(age, growth , weight ):
    #расчёт норм калорий для мужчин
    # return 10 * float(weight) + 6.25 * float(growth) - 5 * float(age) + 5
    # расчёт норм калорий для женщин
    return 10 * float(weight) + 6.25 * float(growth) - 5 * float(age) -161

bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())
class UserState(StatesGroup):
    age = State()
    growth= State()
    weight= State()

@dp.message_handler(text='Calories')
async def set_age(message):
    await message.answer("Введите свой возраст:")
    await UserState.age.set()

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

@dp.message_handler(commands=['start'])
async def start_message(message):
    await message.answer("Привет! Я бот помогающий твоему здоровью.")


@dp.message_handler()
async def all_message(message):
    await message.answer("Введите команду /start, чтобы начать общение.")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)