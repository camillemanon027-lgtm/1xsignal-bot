
import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("⚽ Football", callback_data="football")],
        [InlineKeyboardButton("✈️ Aviator", callback_data="aviator")],
        [InlineKeyboardButton("📊 Statut du bot", callback_data="status")]
    ]

    await update.message.reply_text(
        "🚀 BIENVENUE SUR 1X SIGNAL BOT\n\n"
        "Choisis un module :",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

async def buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "football":
        await query.edit_message_text(
            "⚽ MODULE FOOTBALL\n\n"
            "Statistiques disponibles prochainement.\n"
            "Les données seront présentées sans garantie de résultat."
        )

    elif query.data == "aviator":
        await query.edit_message_text(
            "✈️ MODULE AVIATOR\n\n"
            "Consultation des statistiques historiques uniquement."
        )

    elif query.data == "status":
        await query.edit_message_text("🟢 BOT EN LIGNE")

def main():
    if not TOKEN:
        raise RuntimeError("Token Telegram absent.")

    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(buttons))

    print("1X SIGNAL BOT démarré...")
    app.run_polling()

if __name__ == "__main__":
    main()
