import telebot
import schedule
import time
import datetime

TOKEN = '7663392990:AAE8EdfQyhSmW0sKnHf_2fU-tWHcmBXg2Vg'
chat_id = 1297395673  # ← senin chat ID'in

bot = telebot.TeleBot(TOKEN)

def send_message():
    now = datetime.datetime.now().strftime('%d.%m.%Y %H:%M')
    message = f'📈 B-GAS Sabah Raporu ({now})\n\n"Bugün analiz edilecek hisseler hazırlanıyor..."\n⏳'
    bot.send_message(chat_id, message)

# Her sabah saat 09:30'da çalışması için zamanlayıcı
schedule.every().day.at("09:30").do(send_message)

print("⏰ Bot aktif. Sabah 09:30'u bekliyor...")

while True:
    schedule.run_pending()
    time.sleep(1)
