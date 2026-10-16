import os, json, threading
from flask import Flask
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

TOKEN = os.getenv("BOT_TOKEN")
app = Flask(__name__)

IMOVEIS = {
    "flamboyant": {"nome": "Residencial Flamboyant", "valor": "R$ 12.000", "foto": "em breve"},
    "aldeia": {"nome": "Aldeia do Vale", "valor": "R$ 8.500"}
}

@app.route('/')
def home(): 
    return "RentGhost bot online 24h!"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🏢 Olá! Sou da RentGhost Imóveis de Luxo!\n\nDigite: flamboyant ou aldeia\n\nOu fale o nome do condomínio que procura!")

async def responder(update: Update, context: ContextTypes.DEFAULT_TYPE):
    txt = update.message.text.lower()
    if "flamboyant" in txt:
        await update.message.reply_text(f"🏡 {IMOVEIS['flamboyant']['nome']}\n💰 {IMOVEIS['flamboyant']['valor']}\n\nQuer agendar visita?")
    elif "aldeia" in txt:
        await update.message.reply_text(f"🏡 {IMOVEIS['aldeia']['nome']}\n💰 {IMOVEIS['aldeia']['valor']}")
    else:
        await update.message.reply_text("Anotado! Nossa equipe vai te mandar as opções de luxo no Aldeia e Flamboyant!")

def run_bot():
    bot_app = ApplicationBuilder().token(TOKEN).build()
    bot_app.add_handler(CommandHandler("start", start))
    bot_app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, responder))
    bot_app.run_polling()

if __name__ == "__main__":
    threading.Thread(target=lambda: app.run(host="0.0.0.0", port=8000), daemon=True).start()
    run_bot()
