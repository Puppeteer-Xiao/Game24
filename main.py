import random as rnd
import sys
import time

def print_with_delay(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def generatenumber():
    print("- - - - - - - - - - - -")
    print()
    print("Введите диапазон чисел для генерации случайного числа.")
    while True:
        try:
            numbersrange1 = int(input("Введите число от: "))
            numbersrange2 = int(input("Введите число до: "))
            if numbersrange1 >= numbersrange2:
                print("Ошибка. Число 'от' должно быть меньше числа 'до'. Попробуйте снова.")
                continue
            randomnumber = rnd.randint(numbersrange1, numbersrange2)
            break
        except ValueError:
            print("Ошибка: введите целые числа.")
    print(f"Случайное число сгенерировано в диапазоне от {numbersrange1} до {numbersrange2}")
    return numbersrange1, numbersrange2, randomnumber

def ask_for_repeat(prompt):
    while True:
        try:
            response = int(input(prompt))
            if response in [0, 1]:
                return response
            else:
                print("Введите 0 или 1.")
        except ValueError:
            print("Ошибка: введите 0 или 1.")

def choose_difficulty():
    print("Выберите уровень сложности:")
    print("1 - Легкий (5 попыток)")
    print("2 - Средний (3 попытки)")
    print("3 - Сложный (1 попытка)")
    while True:
        try:
            choice = int(input("Введите 1, 2 или 3: "))
            if choice in [1, 2, 3]:
                if choice == 1:
                    return 5
                elif choice == 2:
                    return 3
                elif choice == 3:
                    return 1
            else:
                print("Введите 1, 2 или 3.")
        except ValueError:
            print("Ошибка: введите 1, 2 или 3.")

def start():
    print("- - - - - - - - - - - -")
    print()
    player_name = input("Введите ваше имя: ")
    print_with_delay(f"Привет, {player_name}! Добро пожаловать в игру 'Угадай число'!", 0.05)
    score = 0
    best_score = 0

    while True:
        difficulty = choose_difficulty()
        hp = difficulty
        numbersrange1, numbersrange2, randomnumber = generatenumber()

        while hp != 0:
            print(f"Ваше хп: {hp}")
            print(f"Ваши очки: {score}")
            try:
                inputnumber = int(input(f"Введите число в диапазоне от {numbersrange1} до {numbersrange2}: "))
            except ValueError:
                print("Ошибка: введите целое число.")
                continue
            
            if inputnumber < numbersrange1 or inputnumber > numbersrange2:
                print("Вы ввели неверное число")
                continue
            else:
                if inputnumber == randomnumber:
                    score += 1
                    if score > best_score:
                        best_score = score
                    if ask_for_repeat("Молодец, ты выиграл! Хочешь сыграть ещё раз? (0 - нет, 1 - да): ") == 0:
                        print_with_delay(f"До свидания, {player_name}! Твои финальные очки: {score}. Лучший результат: {best_score}", 0.05)
                        return
                    else:
                        break
                else:
                    hp -= 1
                    if hp != 0:
                        hint = "меньше" if inputnumber > randomnumber else "больше"
                        print(f"У тебя не получилось угадать число, попробуй ещё раз! Подсказка: загаданное число {hint}.")
                    else:
                        print_with_delay("Проигрыш! Ты потратил все свои попытки.", 0.05)

        if hp == 0:
            if ask_for_repeat("Ты проиграл, хочешь сыграть ещё раз? (0 - нет, 1 - да): ") == 0:
                print_with_delay(f"До свидания, {player_name}! Твои финальные очки: {score}. Лучший результат: {best_score}", 0.05)
                return

start()
