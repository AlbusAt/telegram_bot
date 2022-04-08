from aiogram import Dispatcher, types
from create_bot import bot
from keyboards import kb_client



async def command_start(message : types.Message):
    try:  
        await bot.send_message(message.from_user.id, 'Приятного аппетита', reply_markup=kb_client)
        await message.delete()
    except:
        await message.reply('Общение с ботом через ЛС, напишите ему: \n@Cafe_GauguinBot')
        

async def cafe_work_command(message: types.Message):
    await bot.send_message(message.from_user.id, 'Вс-Чт с 9:00 до 20:00, Пт-Сб с 10:00 до 23:00')
    

async def cafe_place_command(message: types.Message):
    await bot.send_message(message.from_user.id, 'ул. Колбасная 15')
    
def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(cafe_work_command, commands=['Режим_работы'])
    dp.register_message_handler(cafe_place_command, commands=['Расположение'])