import telegram.ext

Token = '5949091762:AAEZ1eQ5BDm8SN0RIcGFvxum4lezOVBi2VM'

updater = telegram.ext.Updater(Token, use_context=True)
dispatcher = updater.dispatcher


def start(update, context):
    update.message.reply_text('Hello, this is a bot for foreigners interested in RUSSIA')


def help(update, context):
    update.message.reply_text(
        """
        /MUSIC ->  TOP SONGS IN RUSSIA
        /WEATHER-> WEATHER FOR THE WEEK
        /PLACES -> PLACES TO VISIT IN RUSSIA
        /WONDERS -> SEVEN WONDERS OF RUSSIA
        /BOOKINGS -> BEST HOTELS TO BOOK IN MOSCOW
        """
    )


def MUSIC(update, context):
    update.message.reply_text("https://kworb.net/charts/apple_s/ru.html")


def WEATHER(update, context):
    update.message.reply_text("https://www.gismeteo.com/weather-moscow-4368/2-weeks/ ")


def PLACES(update, context):
    update.message.reply_text("https://www.planetware.com/russia/best-places-to-visit-in-russia-r-1-2.htm ")


def WONDERS(update, context):
    update.message.reply_text("https://www.russiadiscovery.com/news/seven_wonders_of_russia/")


def BOOKINGS(update, context):
    update.message.reply_text("https://www.visahouse.com/en/booking/hotels-in-russia/")

dispatcher.add_handler(telegram.ext.CommandHandler('start', start))
dispatcher.add_handler(telegram.ext.CommandHandler('music', MUSIC))
dispatcher.add_handler(telegram.ext.CommandHandler('weather', WEATHER))
dispatcher.add_handler(telegram.ext.CommandHandler('places', PLACES))
dispatcher.add_handler(telegram.ext.CommandHandler('wonders', WONDERS))
dispatcher.add_handler(telegram.ext.CommandHandler('Bookings', BOOKINGS))
dispatcher.add_handler(telegram.ext.CommandHandler('help', help))

updater.start_polling()
updater.idle()
