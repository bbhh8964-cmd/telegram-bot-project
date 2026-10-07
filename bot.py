import logging
import asyncio
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# API Token
TOKEN = "8966142556:AAEnl5FIBj5vPeueEVxk9rBCIRi9rtyZ7DA"

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Reply with 'a' to any message"""
    await update.message.reply_text("a")

async def main() -> None:
    """Start the bot"""
    # Create the Application
    application = Application.builder().token(TOKEN).build()

    # Add handlers
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Start the Bot
    await application.initialize()
    await application.start()
    await application.updater.start_polling()
    await application.updater.idle()
    await application.stop()

if __name__ == '__main__':
    asyncio.run(main())
