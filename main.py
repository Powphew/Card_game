
from random import choice
CARD_NUMBER = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
CARD_SUIT = ["Б", "Ч", "П", "Т"]

# 1. приветствие

def welcome():

  print("\nПривет игрок, давай сыграем? ")
  # выбор сложности 
  game_difficulty = input("Выбери уровень сложности: 1. Легко 2. Так себе 3. Жуть ")

  if game_difficulty not in '123':
    print("\nНе корректный выьбор, попробуй еще раз!".upper())
    welcome()
  else:  
    game_difficulty = int(game_difficulty)  
    return game_difficulty


def card_generator():

  random_card_number = choice(CARD_NUMBER)
  random_card_suit = choice(CARD_SUIT)
  return random_card_number, random_card_suit


def user_guess_answer(game_mode):
  game_mode = int(game_mode)
  if game_mode == 1:
    player_answer_suit = input('\nУгадай масть, "Б", "Ч", "П", "Т": ').upper()
    player_answer_number = '0'
    if player_answer_suit not in CARD_SUIT:
      print("\nПожалуйста, выберите карту!")

  elif game_mode == 2:
    player_answer_suit = '0'
    player_answer_number = input("\nУгадайте номер карты: ").upper()
    if player_answer_number not in CARD_NUMBER:
      print("Пожалуйста, выберите карту!")

  else:
    player_answer_suit = input('\nУгадай масть, "Б", "Ч", "П", "Т": ').upper()
    player_answer_number = input("\nУгадай номер карты: ").upper()

    if player_answer_number not in CARD_NUMBER or player_answer_suit not in CARD_SUIT:
      print("\nПожалуйста, выберите карту!")

  return player_answer_suit, player_answer_number


def game_driver(correct_number, correct_suit, player_answer_suit, player_answer_number, game_mode):
  win_count = 0
  lost_count = 0
  if game_mode == 1:
    if player_answer_suit == correct_suit:
      print("\nВы угадали верно!".upper())
      win_count += 1
    else:
      print("\nВы не угадали, попробуем еще разок?")
      lost_count += 1

  elif game_mode == 2:
    if player_answer_number == correct_number:
      print("\nВы угадали верно!".upper())
      win_count += 1
    else:
      print("\nВы не угадали, попробуем еще разок?")
      lost_count += 1

  elif game_mode == 3:
    if player_answer_number == correct_number and player_answer_suit == correct_suit:
      print("\nВы выиграли, вы угадали масть и номер".upper())
      win_count += 1
    else:
      print("\nВы не угадали, попробуем еще разок?!")
      lost_count += 1

  return win_count, lost_count


def user_variables(game_mode):

  game_mode = int(game_mode)

  if game_mode == 1:
    player_answer_suit, player_answer_number = user_guess_answer(game_mode)

  elif game_mode == 2:
    player_answer_suit, player_answer_number = user_guess_answer(game_mode)

  else:
    player_answer_suit, player_answer_number = user_guess_answer(game_mode) 

  return player_answer_suit, player_answer_number

#статистика если нужна.
#def score(count_game, win_count, lost_count):
 # print("GAME OVER")
  #print(f"\n{count_game} игр сыграно")
  #print(f"{win_count} выиграно, {lost_count} проигрышей")
  #print(f"Очков заработано {win_count * 10},  {count_game * 10}")


def game():
  count_game = 0
  win_count = 0
  lost_count = 0

  while True:
    game_mode = welcome()
    correct_number, correct_suit = card_generator()
    player_answer_suit, player_answer_number = user_variables(game_mode)
    win_counter, lost_counter = game_driver(correct_number, correct_suit,
                player_answer_suit, player_answer_number, game_mode)
    win_count += win_counter
    lost_count += lost_counter
    count_game += 1

    is_resume = input("Хотите продолжить? Y/N ").lower()

    if is_resume == 'y':    
      continue
    else:
      out = input("press any key to exit: ")
      print()
      break

 # score(count_game, win_count, lost_count)


game()



# 1. Проверку на дурака (проверка ввода)
# 2. Разные уровни сложности
# 3. Ввод количество раундов