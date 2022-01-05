import telepot

bot = telepot.Bot('1913272827:AAEDSjf8fqNwuJvw8ZXHw5WR41P_re6ti8Q')
# bot.sendMessage('1824238459','안녕하세요')

bot.sendChatAction('1824238459', 'upload_photo')
bot.sendPhoto('1824238459', open('+.png', 'rb'), caption='계산기')