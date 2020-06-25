from random import choice, sample
from time import sleep
from textwrap import dedent
from typing import Generator

def playingBlackjack():
  """I order sequence of my functions

  Returns:
      str : will be performed
  """
  welcome_blackjack(str)
  rules_blackjack('a', 'b')
  choosing_table(int)
  choosing_players('ENTER')
  choosing_cards()
  round_cards()
  check_points()
  
  return print("\nEnd of game!\n")

def welcome_blackjack(str):
  """Will welcome and collect the user name

  Returns:
      str: Will replicate the user name
  """
  print('{:*^126}'.format('\n*** \033[7:30mWelcome to the game Blackjack!\033[m ***\n'),
       f"\n{' '*20}Gabriel Elias© 🇧🇷")
  
  print(dedent(f"""                
                  My name is Jarvis, I'm the dealer.😷
                  How would ou like to be called?
                  """))
  
  global user_name

  user_name = str(input("▶▶▶ ")).strip().title()
  
  print(dedent(f"""
              Mr.{user_name},
              Nice to meet you. Now, let's have fun!
              """))
  
  return

def rules_blackjack(a: str, b:str):
  """Here is contained the rule of the game

  Returns:
      str: choice of option 'a' or 'b'
  """
  print(dedent("""
              Can we proceed to the selection of the game table or would you like to consult the rules?
              [a] Proceed to table selection
              [b] See rules
              """))

  res = str(input("▶▶▶ ")).strip().lower()

  if res == 'a':
    print(dedent(f"""
                Great! Let's proceed to table selection!\n
                *** \033[7:30m. . . processing information . . .\033[m ***\n
                """))
    sleep(2)

  elif res == 'b':
    print(dedent("""
                I understand. Follow the rules below:\n
                *** \033[7:30m. . . processing information . . .\033[m ***
                """))
    sleep(4)

    print(f"\n{'-=-'*40}")
    
    # EAFP
    # Easy Ask Forgiveness than permission.
    # pt-BR: É melhor pedir perdão do que permissão.
    # Try objective: Close file after chanching scenario + treat error if the file is not found.
    try:
      rulestxt = open('deck_rules.txt')
      print(f'{rulestxt.read()}')
      with open("deck_rules.txt") as res:
        res == 'b'
    except FileNotFoundError:
      print("The file does not exist")

    print(dedent(f"""
                {'-=-'*40}
                Well, now that you've consulted the rules, press 'ENTER' to proceed.
                """))
    
    str(input("▶▶▶ ")).strip().title()

    print('\nExcellent choice! Let us proceed then.\n')

    return

  else:
    print_mensage()
    rules_blackjack('a', 'b')

def choosing_table(int):
  """Will choose the numbers of players

  Returns:
      int: will choose one of the options 1,2,3,4
  """
  print(dedent(f"""
              Well, Mr.{user_name}, we have tables for 02 of 05 players.
              Wich table do you whant to join?
              [1] Table for 02 participants
              [2] Table for 03 participants
              [3] Table for 04 participants
              [4] Table for 05 participants
              """))

  global table
  table = int(input('▶▶▶ '))

  if table in (1, 2, 3, 4):
    print(dedent(f"""
                I understand
                \033[4mYou want to play with \033[1m{table+1}\033[m\033[4m more participants.\033[m
                We proceed to the table.
                """))
    
    return

  else:
    print_mensage()
    choosing_table(int)

def choosing_players(ENTER):
  """Radom choice of bot players

  Args:
      ENTER (str): Confirmation
  """
  print("Please, press 'ENTER' to confirm your participation\n")

  input("▶▶▶ ENTER")
  
  print(f"\n👤 Mr.{user_name}, joined this table as a participant")
  sleep(1)
  
  global selected_players

  all_players = f"Mr.{user_name}"
  selected_players = all_players.split(' ')

  bot = ["Mr.Tiago", "Mr.Mateus", "Mr.Pedro", "Mr.João", "Mr.André",
        "Mr.Filipe","Mr.Bartolomeu", "Mr.Tomé", "Mr.Zelote"]

  while len(selected_players) != table+1:
    next_p = choice(bot)
    if next_p not in selected_players:
      print(f"👤 {next_p}, joined this table as a participant")
      selected_players.append(next_p)
      {len(selected_players)}
      sleep(1)

  print(dedent(f"""
              Excellent!
              The table is complete, consisting of {table+1} participants 👥: {' '.join(selected_players)}
              Please, press 'ENTER', to proceed.\n
              """))
  
  input('▶▶▶ ENTER')
  
  return

def choosing_cards():
  """Random card distribution from 02 to 02 plus sum of points
  
  While + if
    Repetition control for lis creation + condition control to not repeat cards
  For - in + If
    repetition control + control condition to assign values and define sum
  """
  nps1 = "A♠ 1♠ 2♠ 3♠ 4♠ 5♠ 6♠ 7♠ 8♠ 9♠ J♠ Q♠ K♠"
  nps2 = "A♣ 1♣ 2♣ 3♣ 4♣ 5♣ 6♣ 7♣ 8♣ 9♣ J♣ Q♣ K♣"
  nps3 = "A♥ 1♥ 2♥ 3♥ 4♥ 5♥ 6♥ 7♥ 8♥ 9♥ J♥ Q♥ K♥"
  nps4 = "A♦ 1♦ 2♦ 3♦ 4♦ 5♦ 6♦ 7♦ 8♦ 9♦ J♦ Q♦ K♦"

  global all_cards
  
  naipes_cards = "A♠ 1♠ 2♠ 3♠ 4♠ 5♠ 6♠ 7♠ 8♠ 9♠ J♠ Q♠ K♠ A♣ 1♣ 2♣ 3♣ 4♣ 5♣ 6♣ 7♣ 8♣ 9♣ J♣ Q♣ K♣ A♥ 1♥ 2♥ 3♥ 4♥ 5♥ 6♥ 7♥ 8♥ 9♥ J♥ Q♥ K♥ A♦ 1♦ 2♦ 3♦ 4♦ 5♦ 6♦ 7♦ 8♦ 9♦ J♦ Q♦ K♦"
  
  all_cards = naipes_cards.split(' ')

  global selected_cards
  
  selected_cards = []

  print(dedent(f"""
              Laides and Gentlemen, follow the 48 cards that make up this deck:
              ╠ Suits of Spades = {nps1}
              ╠ Suits of Clubs = {nps2}
              ╠ Suits of Hearts = {nps3}
              ╚ Suits of Diamonds = {nps4}
              """))
  sleep(2)

  while len(selected_cards) != table +1:
    next_c = sample(all_cards, 2)
    if next_c not in selected_cards:
      selected_cards.append(next_c)
      {len(selected_cards)}

  print("📌 Print below is optional\nSummary of Choosing Cards:")
  for c in range(0, table+1):
    print("Participant: {} | Card hand: {}".format(selected_players[c],' '.join(selected_cards[c])))
  sleep(1)

  points = []

  for pts in range(0, table+1):
    pts = "".join(selected_cards[pts])

    v = (pts[0])
    v1 = (pts[2])

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

    pts = "{}".format(int(v) + int(v1))
    points += [pts]

  print("\n📌 Print below is optional\nFul summary of Choosing Cards:")
  for c in range(0, table+1):
    print("Participant: {} | Card hand: {} | Points: {}"
          .format(selected_players[c],' '.join(selected_cards[c]), points[c]))
  sleep(1)

  print("\nMr.{}, this is your cards {}, that correspond to {} points."
        .format(user_name, ' '.join(selected_cards[0]), points[0]))
  sleep(2)

  return

def round_cards():

  print(dedent("""
              Very good! ツ
              Now that you know your cards and scores, lets's go to the 1ª round.
              Please, press 'ENTER', to proceed.
              """))
  
  input('▶▶▶ ENTER')

  hand_cards = " "
  hand_list = hand_cards.split()

  while len(hand_list) != table + 1:
    next1 = selected_cards.pop(0)
    next2 = ''.join(next1)
    next3 = choice(all_cards)
    next4 = next2 + next3
    hand_list.append(next4)
    {len(hand_list)}

  print(dedent("""
              📌 Print below is optional
              Summary of Round Cards:
              """))
  
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

  print(dedent("""
              📌 Print below is optional
              Full summary of Round Cards:
              """))

  for c in range(0, table+1):
    print("Participant: {} | Card hand: {} | Points: {}"
          .format(selected_players[c], hand_list[c], points1[c]))
  sleep(1)

  print("\nMr.{}, this is your cards {}, that correspond to {} points.\n"
        .format(user_name, ' '.join(hand_list[0]), points1[0]))
  sleep(2)

  return

def check_points():
  """Sum of points and definition of winner and loser"""

  print("Please, press 'ENTER', to proceed.")
  
  input('▶▶▶ ENTER')

  print("\nLadies and Gentlemen, are there any participants wish to declare victory?")
  sleep(2)

  for c in range(0, table + 1):

    if points1[c] >= "21":
      print("\n{}: YESS, I WIN!!\nCongratulations, {}! Your score is {}, this is above {}."
            .format(selected_players[c], selected_players[c], points1[c], 21))
      sleep(2)
  
    else:
      print("\nI understand!\n{}, your score is {}, was {} points from victory."
            .format(selected_players[c], points1[c], 21 - int(points1[c])))
      sleep(2)

  print(dedent("""
              \nThe Gaming House thanks everyone for their participation!
              \nWe hope to see you in an upcoming game.
              """))

  return

def print_mensage():
    print("\nI'm sorry, this option is not valid. Try again.\n")

playingBlackjack()
