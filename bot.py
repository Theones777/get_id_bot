import asyncio

from bot_init import dp, bot
from handlers import register_handlers_common, set_commands


async def main():
    register_handlers_common(dp)
    await set_commands(bot)
    await dp.start_polling()

if __name__ == '__main__':
    asyncio.run(main())
