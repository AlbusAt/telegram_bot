from aiogram import Dispatcher,types

async def echo_send(message : types.Message):
    if (message):
        await message.delete()
    
def register_handlers_other(dp: Dispatcher):
    dp.register_message_handler(echo_send)
