import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🚀 1X SIGNAL BOT\n\n"
        "Bot connecté !\n\n"
        "/football - Module football\n"
        "/aviator - Module Aviator\n"
        "/status - État du bot"
    )

async def football(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "⚽ Module Football activé.\nAnalyse des cotes en préparation."
    )

async def aviator(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "✈️ Module Aviator activé.\nStatistiques en préparation."
    )

async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🟢 BOT EN LIGNE")

def main():
    if not TOKEN:
        raise RuntimeError("Token Telegram absent.")

    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("football", football))
    app.add_handler(CommandHandler("aviator", aviator))
    app.add_handler(CommandHandler("status", status))

    print("1X SIGNAL BOT démarré...")
    app.run_polling()

if __name__ == "__main__":
    main()