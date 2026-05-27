import asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

MY_ID = "1623105401"
TOKEN = "8902474076:AAFNVaUE20yFemw_o_HBWoV3DHLHqybnsP8"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    await context.bot.send_message(chat_id=MY_ID, text=f"دخل: {user.first_name}")
    await update.message.reply_text("مرحباً!")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.run_polling()
