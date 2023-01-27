import json

from aiogram import types, Dispatcher, Bot
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.types import BotCommand

from states import Ids


async def set_commands(bot: Bot):
    commands = [
        BotCommand(command="/start", description="Выбрать задачу"),
        BotCommand(command="/cancel", description="Вернуться в начало")
    ]
    await bot.set_my_commands(commands)


async def cmd_cancel(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer("Сброс бота", reply_markup=types.ReplyKeyboardRemove())


async def bot_start(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer("Введите, пожалуйста, ваше Имя и Фамилию")
    await state.set_state(Ids.waiting_for_name.state)


async def name_insert(message: types.Message, state: FSMContext):
    await message.answer("Теперь, пожалуйста, введите ваш id разметчика")
    await state.update_data(name=message.text)
    await state.set_state(Ids.waiting_for_id.state)


async def id_insert(message: types.Message, state: FSMContext):
    await message.answer("Спасибо")
    user_data = await state.get_data()
    name = user_data['name']
    marker_id = message.text
    with open('ids.json', encoding='utf-8') as f:
        ids_list = json.load(f)
        ids_list.append({message.from_user.id: [marker_id, name]})
    with open('ids.json', 'w', encoding='utf-8') as f:
        json.dump(ids_list, f)
    await state.finish()


def register_handlers_common(dp: Dispatcher):
    dp.register_message_handler(bot_start, commands="start", state="*")
    dp.register_message_handler(cmd_cancel, commands="cancel", state="*")
    dp.register_message_handler(name_insert, state=Ids.waiting_for_name)
    dp.register_message_handler(id_insert, state=Ids.waiting_for_id)
    dp.register_message_handler(cmd_cancel, Text(equals="отмена", ignore_case=True), state="*")
