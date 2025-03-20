from pyrogram import Client

async def main():
    bot = Client("bot")
    await bot.start()

asyncio.run(main())
