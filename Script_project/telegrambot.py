import telepot

token = '1238627505:AAEQPKXQg1rglXLITWyef7d5NSmbE1OGIzg'
bot = telepot.Bot(token)
updates = bot.getUpdates()


bot.sendMessage(mc, "안녕하세요~")
bot.sendMessage(dj, "안녕하세요~")