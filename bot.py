import telebot
import schedule
import time
import datetime
import os

# Ortam değişkenlerinden token ve chat_id alınıyor
TOKEN = os.getenv('TOKEN')
chat_id = int(os.getenv('CHAT_ID'))

bot = telebot.TeleBot(TOKEN)

def send_message():
    now = datetime.datetime.now().strftime('%d.%m.%Y %H:%M')
    message = f"📈 B-GAS Sabah Raporu ({now})\n\nBugün analiz edilecek hisseler hazırlanıyor...\n⏳"
    bot.send_message(chat_id, message)

schedule.every().day.at("09:30").do(send_message)

print("⏰ Bot Railway'de aktif. Sabah 09:30'u bekliyor...")

while True:
    schedule.run_pending()
    time.sleep(1)
