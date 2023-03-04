import time
import random

#лотерея

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
true_number = 0

res = 'Да'
while res == 'Да':
    print('Лотерея! Будет загадано победное число! Напишите "ДА" для участия!:')
    urnum_gen = input(': ')
    if urnum_gen == 'ДА':
        win_numbers = random.choice(numbers)
        true_number += win_numbers
        print('Генерация... Подождите...')
        time.sleep(3)
        print('---------------------------------------------------------------')
        print('Число загадано!.')
        print('---------------------------------------------------------------')
    
    if urnum_gen == 'debug':
        win_numbers = random.choice(numbers)
        true_number += win_numbers
        print('Activate Debug Mode... ')
        time.sleep(2.5)
        print(f'Debug result: Right Numbers = {win_numbers}')
        time.sleep(2)
        print('Ending of Debug')
    

    time.sleep(1)
    inputnum = int(input('Введите число от 1 до 15: '))

    if inputnum == true_number:
        print('------------------------------------------------------')
        print('Ваше число победное! Мы отправили приз вам на почту!.')
        time.sleep(10)
        exit()
    else: 
        print('------------')
        print('Число проигрышное, попробуйте снова!')
res = input('Купить лотерейный билет? [ДА|НЕТ]: ')
    
    