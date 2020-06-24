from random import choice, sample
from time import sleep

def playingBlackjack():
  """Sequência de execução das Funções"""
  welcome21 = welcome_blackjack()
  rules21 = rules_blackjack()
  table21 = choosing_table()
  players21 = choosing_players()
  cards21 = choosing_cards()
  round21 = round_cards()
  check21 = check_points()
  return print("\nEnd of game!\n")

def welcome_blackjack():
  """Welcome + input(user name)"""
  print('{:*^126}'.format('\n*** \033[7:30mWelcome to the game Blackjack!\033[m ***\n'))
  print(f"{' '*20}Gabriel Elias© 🇧🇷")
  print("\nMy name is Jarvis, I'm the dealer.😷\nHow would ou like to be called?")

  global user_name

  user_name = str(input("▶▶▶ ")).strip().title()
  return print(f"\nMr.{user_name},\nNice to meet you. Now, let's have fun!\n")

def rules_blackjack():
  """Open the game rule"""
  print("Can we proceed to the selection of the game table or would you like to consult the rules?"
        "\n[a] Proceed to table selection\n[b] See rules")

  res = str(input("▶▶▶ ")).strip().lower()

  if res == 'a':
    print(f"\nGreat! Let's proceed to table selection!\n")

    print('\n*** \033[7:30m. . . processing information . . .\033[m ***\n')
    return sleep(2)

  elif res == 'b':
    rulestxt = open('deck_rules.txt')
    print("\nI understand. Follow the rules below:\n"
         f"\n*** \033[7:30m. . . processing information . . .\033[m ***\n")
    sleep(4)

    print(f"\n{'-=-'*40}\n{rulestxt.read()}{'-=-'*40}\n"
           "\nWell, now that you've consulted the rules, press 'ENTER' to proceed.")

    str(input("▶▶▶ ")).strip().title()

    return print('\nExcellent choice! Let us proceed then.\n')

  else:
    print_mensage()
    rules_blackjack()

def choosing_table():
  """Define number of players"""
  print(f"Well, Mr.{user_name}, we have tables for 02 of 05 players.\nWich table do you whant to join?"
         "\n[1] Table for 02 participants\n[2] Table for 03 participants"
         "\n[3] Table for 04 participants\n[4] Table for 05 participants\n")

  global table
  table = int(input('▶▶▶ '))

  if table in (1, 2, 3, 4):
    return print("\nI understand."
                f"\n\033[4mYou want to play with \033[1m{table+1}\033[m\033[4m more participants.\033[m"
                 "\nWe proceed to the table.\n")

  else:
    print_mensage()
    choosing_table()

def choosing_players():
  """Choice of bot players"""
  print("Please, press 'ENTER' to confirm your participation.")
  input("▶▶▶ ")
  print(f"\n👤 Mr.{user_name}, joined this table as a participant.")

  global selected_players

  all_players = f"Mr.{user_name}"
  selected_players = all_players.split(' ')

  bot = ["Mr.Tiago", "Mr.Mateus", "Mr.Pedro", "Mr.João", "Mr.André", "Mr.Filipe", "Mr.Bartolomeu", "Mr.Tomé", "Mr.Zelote"]

  while len(selected_players) != table+1:
    next_p = choice(bot)
    if next_p in selected_players:
      pass
    else:
      print("👤 {}, joined this table as a participant.".format(next_p))
      selected_players.append(next_p)
      {len(selected_players)}
      sleep(1)

  return print(f"\nExcellent!\nThe table is complete, consisting of {table+1} participants 👥: "
               f"{' '.join(selected_players)}.\n\nPlease, press 'ENTER', to proceed."),input('▶▶▶ ')

def choosing_cards():
  """Random choice of cards"""
  nps1 = "A♠ 1♠ 2♠ 3♠ 4♠ 5♠ 6♠ 7♠ 8♠ 9♠ J♠ Q♠ K♠"
  nps2 = "A♣ 1♣ 2♣ 3♣ 4♣ 5♣ 6♣ 7♣ 8♣ 9♣ J♣ Q♣ K♣"
  nps3 = "A♥ 1♥ 2♥ 3♥ 4♥ 5♥ 6♥ 7♥ 8♥ 9♥ J♥ Q♥ K♥"
  nps4 = "A♦ 1♦ 2♦ 3♦ 4♦ 5♦ 6♦ 7♦ 8♦ 9♦ J♦ Q♦ K♦"

  global all_cards
  naipes_cards = "A♠ 1♠ 2♠ 3♠ 4♠ 5♠ 6♠ 7♠ 8♠ 9♠ J♠ Q♠ K♠ A♣ 1♣ 2♣ 3♣ 4♣ 5♣ 6♣ 7♣ 8♣ 9♣ J♣ Q♣ K♣ A♥ 1♥ 2♥ 3♥ 4♥ 5♥ 6♥ 7♥ 8♥ 9♥ J♥ Q♥ K♥ A♦ 1♦ 2♦ 3♦ 4♦ 5♦ 6♦ 7♦ 8♦ 9♦ J♦ Q♦ K♦"
  all_cards = naipes_cards.split(' ')

  global selected_cards
  selected_cards = []

  print("\nLaides and Gentlemen, segue as 48 cartas que copõem a partida:"
        "\n╠ Suits of Spades = {}\n╠ Suits of Clubs = {}\n╠ Suits of Hearts = {}\n╚ Suits of Diamonds = {}\n"
        .format(nps1,nps2,nps3,nps4))
  sleep(2)

  while len(selected_cards) != table +1:
    next_c = sample(all_cards, 2)
    selected_cards.append(next_c)
    {len(selected_cards)}

  print("📌 Print below is optional\nSummary of Choosing Cards:")
  for c in range(0, table+1):
    print("Participant: {} | Card hand: {}"
    .format(selected_players[c],' '.join(selected_cards[c])))
  sleep(1)

  points = []

  for pts in range(0, table+1):
    pts = "".join(selected_cards[pts])

    v = (pts[0])
    v1 = (pts[2])
# O metodo de controle seguinte na distrbuição das 03 cartas é mais simples e funcional.
# Esse é bem trabalhoso, não remodulei para te mostrar a evolução na construção do código...
    if v in "J,Q,K":
      v = 10
      if v1 == "A":
        v1 = 1
        ("Soma:{}".format(int(v)+int(v1)))
      elif v1 in "J,Q,K":
        v1 = 10
        ("Soma:{}".format(int(v)+int(v1)))
      else:
        ("Soma:{}".format(int(v)+int(v1)))

    if v == "A":
      v = 1
      if v1 == "A":
        v1 = 1
        ("Soma:{}".format(int(v)+int(v1)))
      elif v1 in "J,Q,K":
        v1 = 10
        ("Soma:{}".format(int(v)+int(v1)))
      else:
        ("Soma:{}".format(int(v)+int(v1)))

    if v in ("1","2","3","4","5","6","7","8","9"):
      if v1 == "A":
        v1 = 1
        ("Soma:{}".format(int(v)+int(v1)))
      elif v1 in "J,Q,K":
        v1 = 10
        ("Soma:{}".format(int(v)+int(v1)))
      else:
        ("Soma:{}".format(int(v)+int(v1)))

    pts = "{}".format(int(v) + int(v1))
    points += [pts]

  print("\n📌 Print below is optional\nFul summary of Choosing Cards:")
  for c in range(0, table+1):
    print("Participant: {} | Card hand: {} | Points: {}"
          .format(selected_players[c],' '.join(selected_cards[c]), points[c]))
  sleep(1)

  print("\nMr.{}, this is your cards {}, that correspond to {} points."
        .format(user_name, ' '.join(selected_cards[0]), points[0]))
  return sleep(2)

def round_cards():

  print("\nVery good! ツ\nNow that you know your cards and scores, lets's go to the 1ª round.\n"
        "\nPlease, press 'ENTER', to proceed."),input('▶▶▶ ')

  hand_cards = " "
  hand_list = hand_cards.split()

  while len(hand_list) != table + 1:
    next1 = selected_cards.pop(0)
    next2 = ''.join(next1)
    next3 = choice(all_cards)
    next4 = next2 + next3
    hand_list.append(next4)
    {len(hand_list)}

  print("\n📌 Print below is optional\n\nSummary of Round Cards:")
  for c in range(0, table+1):
    print("Participant: {} | Card hand: {}"
    .format(selected_players[c],hand_list[c]))
  sleep(1)

  global points1
  points1 = []
  for pts in range(0, table+1):
    pts = hand_list[pts]

    v = (pts[0])
    v1 = (pts[2])
    v2 = (pts[4])

    if v in 'J,Q,K':
      v = 10
    if v == 'A':
      v = int(1)
    if v == "1,2,3,4,5,6,7,8,9":
      v = v

    if v1 in 'J,Q,K':
      v1 = 10
    if v1 == 'A':
      v1 = int(1)
    if v1 == "1,2,3,4,5,6,7,8,9":
      v1 = v1

    if v2 in 'J,Q,K':
      v2 = 10
    if v2 == 'A':
      v2 = int(1)
    if v2 == "1,2,3,4,5,6,7,8,9":
      v2 = v2

    p = "{}".format(int(v) + int(v1) + int(v2))
    points1 += [p]

  print("\n📌 Print below is optional\n\nFull summary of Round Cards:")
  for c in range(0, table+1):
    print("Participant: {} | Card hand: {} | Points: {}"
          .format(selected_players[c], hand_list[c], points1[c]))
  sleep(1)

  print("\nMr.{}, this is your cards {}, that correspond to {} points.\n"
        .format(user_name, ' '.join(hand_list[0]), points1[0]))

  return sleep(2)

def check_points():
  print("Please, press 'ENTER', to proceed."),input('▶▶▶ ')
  print("\nLadies and Gentlemen, are there any participants wish to declare victory?")
  sleep(2)

  for c in range(0, table + 1):

    if points1[c] >= "21":
      print("\n{}: YESS, I WIN!!\nCongratulations, {}! Your score is {}, this is above {}."
            .format(selected_players[c], selected_players[c], points1[c], 21))
      sleep(1)
    else:
      print("\nI understand!\n{}, your score is {}, was {} points from victory."
            .format(selected_players[c], points1[c], 21 - int(points1[c])))
      sleep(1)

  return print("\nThe Gaming House thanks everyone for their participation!\n"
        "\nWe hope to see you in an upcoming game.")

def print_mensage():
    print("\nMe desculpe. Não compreende o que você disse.\n")

playingBlackjack()
