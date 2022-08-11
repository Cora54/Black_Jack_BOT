import random, telebot

bot = telebot.TeleBot('5499853268:AAErf-qMWqQ750Z9XJFdYqPqfHjefD5ENRg')
from Balance import balance
from Balance import money, a


def game(user_id):
  print(user_id)
  balance(bot, user_id)
  bot.send_message(user_id, 'Введите ставку:')
  
  srt = yield 0
  
  st = int(srt)

  k = []

  for i in range(1, 11):
    k.append(i)
    k.append(i)
    k.append(i)
    k.append(i)
    k += [10] * 12
    random.shuffle(k)

    def ppp(koloda):
      card = k.pop()
      if card == 1:
        card = 11
        if 11 in koloda:
          card = 1
          koloda.append(card)
          d = []
          p = []
          ppp(d)
          ppp(p)
          ppp(d)
          ppp(p)
          bot.send_message(user_id, f'{ d [0] }-?')

          while True:
            bot.send_message(user_id, f'Еще карту?\n{p}')
            s = sum(p)
            s1 = sum(d)
            if s > 21:
              bot.send_message(user_id, f'Перебор\n{s}')
              money(bot, user_id, 'Перебор', st)
            break
            keyboard = telebot.types.InlineKeyboardMarkup([[
            telebot.types.InlineKeyboardButton(
                'Еще', callback_data="yes"),
            telebot.types.InlineKeyboardButton(
                'Стоп',
            callback_data='notyes'  #ОДНА ИЗ КНОПОК 
            )
        ]])
            bot.send_message(user_id,'Еще карту?',reply_markup=keyboard)
        inp = yield 0  # ------- 1
        if inp == 'yes':
          p = p + [k.pop()]
        continue
        bot.send_message(user_id, f'{d}\n{p}')
        if s > s1:
          bot.send_message(user_id, 'Победа!')
          money(bot, user_id, 'Победа', st)
        break
        bot.send_message(user_id, 'Поражение')
        money(bot, user_id, 'Поражение', st)
        break

      g = {}
      @bot.message_handler(commands=["start"])
      def start(m):
        g[m.chat.id] = game(m.chat.id)
        g[m.chat.id].send(None)

        #КНОПКУ СЮДА

        @bot.callback_query_handler(func=lambda call: True)
        def callback_inline(call):
          user_id = call.message.chat.id
        try:
          
          g[user_id].send(call.data)  # --------- 1
          
        except:
            g[user_id] = game(user_id)
            g[user_id].send(None)
            @bot.message_handler()
            def stavka(m):
              if m.text.startswith('/gift '):
                [com, idd, gift] = m.text.split()
                idd = int(idd)
                print(idd, a)
                a[idd] = a[idd] + int(gift)
                
              return
              
              user_id = m.chat.id
              g[user_id].send(m.text)  # ---------------- 2
              bot.polling(none_stop=True, interval=0)
