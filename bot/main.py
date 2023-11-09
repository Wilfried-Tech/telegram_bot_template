import asyncio
import logging
from os import getenv

from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

from bot import _run_app

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
# set higher logging level for httpx to avoid all GET and POST requests being logged
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_html(text="hello world!")


async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_html(text="An error occur")


def start_bot(data=None):
    application = Application.builder().token(getenv("TOKEN")).build()

    # Add handlers
    application.add_handler(CommandHandler("start", start))
    application.add_error_handler(error_handler)

    _run_app(application, data)


if __name__ == "__main__":
    start_bot()
