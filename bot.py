import os
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import Application, CommandHandler, ContextTypes

BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
WEBAPP_URL = "https://one-sepia-12.vercel.app"

logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    args = context.args
    ref_code = args[0] if args else None
    logger.info(f"🎁 ref: {ref_code}")
    
    if ref_code:
        webapp_url = f"{WEBAPP_URL}?ref={ref_code}"
        message_text = (
            "💰 **টাকা কামাও**-এ স্বাগতম!\n\n"
            "🎁 আপনি **৳50 রেফারেল বোনাস** পাবেন!\n\n"
            "👇 নিচের বাটনে ক্লিক করুন"
        )
    else:
        webapp_url = WEBAPP_URL
        message_text = (
            "💰 **টাকা কামাও**-এ স্বাগতম!\n\n"
            "🎯 প্রতিদিন টাকা আয় করুন:\n"
            "• 🧠 কুইজ খেলে\n"
            "• 🎯 টাস্ক করে\n"
            "• 👥 বন্ধু রেফার করে\n\n"
            "👇 নিচের বাটনে ক্লিক করুন"
        )
    
    logger.info(f"🔗 URL: {webapp_url}")
    
    keyboard = [[
        InlineKeyboardButton(
            "🚀 Earn Now",
            web_app=WebAppInfo(url=webapp_url)
        )
    ]]
    
    await update.message.reply_text(
        message_text,
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode="Markdown"
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("💰 টাকা কামাও Bot\n\n/start পাঠান।")


def main():
    if not BOT_TOKEN:
        logger.error("❌ BOT_TOKEN নেই!")
        return
    logger.info("🚀 Bot চালু হচ্ছে...")
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    logger.info("✅ Bot চালু হয়েছে!")
    app.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
