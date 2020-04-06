
def main():
  done = True
  if done:
    return
    # quit/stop/exit
 # else:
    # do other stuff


print('Вы часто посещаете мироприятия?')
c = input()
if c == 'нет' or c == 'да':
    print('Вы часто слушаете музыку?')
    a = input()
else: pass
if a == 'да' or a == 'нет':
    print('Вы играете в компьютерные игры?')
    b = input()
else:
    


if b == 'да' or b == 'нет':
    print('У вас много друзей?')
    f = input()
else: pass
if b == 'да' or b == 'нет':
   print('Подсчет результатов. Ждите...')
else: pass
if (a == 'да' and c == 'да' and b == 'нет' and f == 'нет'):
    print('Вы довольно общительный человек')
elif (a == 'да' and c == 'да' and b == 'да' and f == 'да'):
    print('Вы очень разносторонний человек')
elif (a == 'да' and c == 'нет' and b == 'нет' and f == 'да'):
    print('Вы музыкальный человек')
elif (a == 'нет' and c == 'нет' and b == 'нет' and f == 'нет'):
    print('Вы человек вообще?')
elif (a == 'нет' and c == 'нет' and b == 'нет' and f == 'да'):
    print('Друзья-ваше все')
elif (a == 'нет' and c == 'нет' and b == 'да' and f == 'нет'):
    print('Вы профи в своем деле, но не злоупотребляйте этим')
else:
    print('Вы хороший человек')
