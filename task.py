# MyProfile app

SEPARATOR = '------------------------------------------'

# user profile
n = ''
a = 0
ph = ''
e = ''
i = ''
# social links
v = ''
t = ''
tk = ''

print('Приложение MyProfile')
print('Сохраняй информацию о себе и выводи ее в разных форматах')

while True:
    # main menu
    print(SEPARATOR)
    print('ГЛАВНОЕ МЕНЮ')
    print('1 - Ввести или обновить информацию')
    print('2 - Вывести информацию')
    print('0 - Завершить работу')

    option = int(input('Введите номер пункта меню: '))
    if option == 0:
            break

    if option == 1:
        # submenu 1: edit info
        while True:
            print(SEPARATOR)
            print('ВВЕСТИ ИЛИ ОБНОВИТЬ ИНФОРМАЦИЮ')
            print('1 - Общая информация')
            print('2 - Социальные сети и мессенджеры')
            print('0 - Назад')

            option2 = int(input('Введите номер пункта меню: '))
            if option2 == 0:
                break
            if option2 == 1:
                # input general info
                n = input('Введите имя: ')
                while 1:
                        # validate user age
                        a = int(input('Введите возраст: '))
                        if a > 0:
                            break
                        print('Возраст должен быть положительным')

                uph = input('Введите номер телефона (+7ХХХХХХХХХХ): ')
                ph = ''
                for ch in uph:
                    if ch == '+' or ('0' <= ch <= '9'):
                        ph += ch


                e = input('Введите адрес электронной почты: ')
                i = input('Введите дополнительную информацию:\n')

            elif option2 == 2:
                # input social links
                v = input('Введите адрес профиля Вконтакте: ')
                t = input('Введите логин Telegram: ')
                tk = input('Введите логин Tiktok: ')
            else: print('Введите корректный пункт меню')
    elif option == 2:
        # submenu 2: print info
        while True:
            print(SEPARATOR)
            print('ВЫВЕСТИ ИНФОРМАЦИЮ')
            print('1 - Общая информация')
            print('2 - Вся информация')
            print('0 - Назад')

            option2 = int(input('Введите номер пункта меню: '))
            if option2 == 0:
                break
            if option2 == 1:
                # print general information
                print(SEPARATOR)
                print('Имя:    ', n)
                if 11 <= a % 100 <= 19: years_name = 'лет'
                elif a % 10 == 1: years_name = 'год'
                elif 2 <= a % 10 <= 4: years_name = 'года'
                else: years_name = 'лет'


                print('Возраст:', a, years_name)
                print('Телефон:', ph)
                print('E-mail: ', e)
                if i:
                        print('')
                        print('Дополнительная информация:')
                        print(i)

            elif option2 == 2:
                # print full information
                print(SEPARATOR)
                print('Имя:    ', n)
                if 11 <= a % 100 <= 19:    years = 'лет'
                elif a % 10 == 1:    years = 'год'
                elif 2 <= a % 10 <= 4:      years = 'года'
                else:  years = 'лет'
                print('Возраст:', a, years)
                print('Телефон:', ph)
                print('E-mail: ', e)
                if i:
                            print('')
                            print('Дополнительная информация:')
                            print(i)

                # print social links
                print('')
                print('Социальные сети и мессенджеры')
                print('Вконтакте:', v)
                print('Telegram: ', t)
                print('Tiktok:   ', tk)
            else:   print('Введите корректный пункт меню')
    else:       print('Введите корректный пункт меню')
