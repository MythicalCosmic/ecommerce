"""
Main bot entry point
"""
import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from dotenv import load_dotenv

from core.config import config
from core.logging import setup_logging
from database.database import init_db
from bot.handlers import register_handlers

load_dotenv()
setup_logging()

logger = logging.getLogger(__name__)

async def main():
    """Initialize and start the bot"""
    bot = Bot(token=config.bot_token, parse_mode=ParseMode.HTML)
    dp = Dispatcher()
    
    await init_db()
    logger.info("Database initialized")
    
    register_handlers(dp)
    logger.info("Handlers registered")
    
    logger.info("Bot started")
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("Bot stopped")
