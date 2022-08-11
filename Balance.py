

a = {}
def balance(bot, user_id):
  if user_id not in a:
    a[user_id] = 25
  bot.send_message(user_id,f'Ваш баланс:{a[user_id]}$')
def money(bot, user_id, uslovie,st):
  if uslovie == 'Победа':
    a[user_id] += st
  elif uslovie == 'Перебор':
    a[user_id] -= st
  elif uslovie == 'Поражение':
    a[user_id] -= st


  
  