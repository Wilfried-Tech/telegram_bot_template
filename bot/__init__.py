import asyncio
from os import getenv

from telegram import Update
from telegram.ext import Application

__all__ = ['_run_app']


def _run_app(application: Application, data: dict):
    if data is None:
        return application.run_polling()
    else:
        async def run_webhook():
            await application.bot.set_webhook(url=getenv("WEBHOOK"))
            await application.update_queue.put(Update.de_json(data=data, bot=application.bot))
            async with application:
                await application.start()
                await application.stop()

        asyncio.run(run_webhook())
