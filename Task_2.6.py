import random
number = random.randint(1, 100)
user_input = None
count = 0


def game(count=1):
    if count > 10:
        print('Вы проиграли')
        return True
    else:
        print("Попытка №", count)
        user_input = int(input("Введите число: "))
        if user_input == number:
            print(f'Поздравляем, Вы угадали число')
            return True
        elif number < user_input:
            print("Ваше число больше загаданного")
            return game(count+1)
        elif number > user_input:
            print("Ваше число меньше загаданного ")
            return game(count+1)

game()