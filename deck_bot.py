import random

rulestxt = open('deck_rules.txt')

def playingBlackjack():
  """Sequência de execução das Funções"""
  welcome = welcome_blackjack()
  rules = rules_blackjack()
  table = choosing_table()
  players = choosing_players()
  cards = choosing_cards()


def welcome_blackjack():
  """Welcome + input(user name)"""
  print("**********************************\n***Bem-vindo ao Game Blackjack!***\n**********************************\n")
  print("Chamo-me Jarvis, sou o croupier.\nComo gostaria de ser chamado(a)?")

  global user_name
  user_name = input(">>> ")
  return print(f"\nMr.{user_name},\nAgora que fomos devidamente apresentados, vamos a diversão!\n")

def rules_blackjack():
  """Open the game rule"""
  res = input("Podemos seguir para seleção da mesa de jogos ou gostaria de consultar as regras?\n[a] Prosseguir para seleção da mesa \n[b] Consultar regras\n>>>")
  if res == 'a':
    return print('\nExcelente. Prossigamos para seleção da mesa!\n')
  elif res == 'b':
    return print(f'\nÓtimo, segue abaixo as regras: {rulestxt.read()}'
    '\nBom, agora que já consultou as regras:\nCaso não deseje prosseguir, aperte "CTRL + C".\n'
    'Agora, se deseja prosseguir, aperte "ENTER", para irmos para seleção de mesa.'),input(">>> "),print('\nExcelente escolha! Prossigamos então.\n')
  else:
      print_mensage()
      rules_blackjack()

def choosing_table():
  """Define number of players"""
  print(f"Pois bem, Mr.{user_name}, dispomos de mesas de 02 à 05 jogadores.\nDeseja sentar-se em qual mesa?\n[1] Mesa para 02 participantes\n[2] Mesa para 03 participantes\n[3] Mesa para 04 participantes\n[4] Mesa para 05 participantes\n")
  global table
  table = int(input('>>> '))
  if table == int('1'):
    return print("Compreendo.\nDeseja jogar com mais 01 participante.\nProssigamos para mesa!\n")
  elif table == int('2'):
    return print("Compreendo.\nDeseja jogar com mais 02 participantes.\nProssigamos para mesa!\n")
  elif table == int('3'):
    return print("Compreendo.\nDeseja jogar com mais 03 participantes.\nProssigamos para mesa!\n")
  elif table == int('4'):
    return print("Compreendo.\nDeseja jogar com mais 04 participantes.\nProssigamos para mesa!\n")
  else:
      print_mensage()
      choosing_table()

def choosing_players():
  """Random choice of bot players"""
  print('Por gentileza, aperte "ENTER", para confirmar sua participação.')
  input(">>> ")
  print(f"Mr.{user_name}, juntou-se a mesa como participante.")

  global selected_players

  all_players = f"Mr.{user_name}"
  selected_players = all_players.split(' ')

  bot = "Mr.Tiago Mr.Mateus Mr.Pedro Mr.João Mr.André Mr.Filipe Mr.Bartolomeu Mr.Tomé Mr.Zelote"
  bot_players = bot.split(' ')

  while len(selected_players) != table + 1:
    proximo = random.choice(bot_players)
    print(proximo,", juntou-se a esta mesa como parcitipante")
    selected_players.append(proximo)
    proximo = bot_players.pop()
    {len(selected_players)}

  global bot1, bot2, bot3, bot4

  bot1 = selected_players[1]
  bot2 = selected_players[2]
  bot3 = selected_players[3]
  bot4 = selected_players[4]

  return print(f'\nExcelete!\nA mesa está completa, composta pelos {table+1} participantes: {selected_players}\n'
  'Por gentileza, aperte "ENTER", para prosseguirmos.'),input(">>> ")

def choosing_cards():
  """Random choice of cards"""
  naip_espada = "A♠ 1♠ 2♠ 3♠ 4♠ 5♠ 6♠ 7♠ 8♠ 9♠ 10♠ J♠ Q♠ K♠"
  naip_paus = "A♣ 1♣ 2♣ 3♣ 4♣ 5♣ 6♣ 7♣ 8♣ 9♣ 10♣ J♣ Q♣ K♣"
  naip_copas = "A♥ 1♥ 2♥ 3♥ 4♥ 5♥ 6♥ 7♥ 8♥ 9♥ 10♥ J♥ Q♥ K♥"
  naip_ouro = "A♦ 1♦ 2♦ 3♦ 4♦ 5♦ 6♦ 7♦ 8♦ 9♦ 10♦ J♦ Q♦ K♦"

  naipes_cards = f"{naip_espada,naip_paus,naip_copas,naip_ouro}"

  global cards

  cards = naipes_cards.split(' ')
  print(f"\nLaides and Gentlemen, segue as 52 cartas que copõem a partida:\n\n{naipes_cards.split(',,,')}\n")

  user_cards = random.sample(cards, 2)

  print('Neste momento as cartas serão distriuidas, sendo 02 para cada participante, segundo a "regra".\nEstas são as suas cartas:\n>>> {}\n'.format(user_cards))

  print('O "print" das cartas dos bots são meramente ilustrativa.')
  bot1_cards = random.sample(cards, 2)
  print(f'Hand de {bot1}: ''{}'.format(bot1_cards))
  bot2_cards = random.sample(cards, 2)
  print(f'Hand de {bot2}: ''{}'.format(bot2_cards))
  bot3_cards = random.sample(cards, 2)
  print(f'Hand de {bot3}: ''{}'.format(bot3_cards))
  bot4_cards = random.sample(cards, 2)
  return print(f'Hand de {bot4}: ''{}'.format(bot4_cards))

def print_mensage():
    print("\nMe desculpe. Não compreende o que você disse.\n")

playingBlackjack()
