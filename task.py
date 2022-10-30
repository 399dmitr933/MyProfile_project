# MyProfile app

SEPARATOR = '------------------------------------------'

# user profile
input_name = ''
input_age = 0
input_phone = ''
input_e_mail = ''
input_info = ''


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
                input_name = input('Введите имя: ')
                while 1:
                    # validate user age
                    input_age = int(input('Введите возраст: '))
                    if input_age > 0:
                        break
                    print('Возраст должен быть положительным')

                check_phone = input('Введите номер телефона (+7ХХХХХХХХХХ): ')
                for i_char in check_phone:
                    if i_char == '+' or ('0' <= i_char <= '9'):
                        input_phone += i_char

                input_e_mail = input('Введите адрес электронной почты: ')
                input_info = input('Введите дополнительную информацию:\n')

            elif option2 == 2:
                # input social links
                break
            else:
                print('Введите корректный пункт меню')
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
                print('Имя:    ', input_name)
                if 11 <= input_age % 100 <= 19:
                    years_name = 'лет'
                elif input_age % 10 == 1:
                    years_name = 'год'
                elif 2 <= input_age % 10 <= 4:
                    years_name = 'года'
                else:
                    years_name = 'лет'

                print('Возраст:', input_age, years_name)
                print('Телефон:', input_phone)
                print('E-mail: ', input_e_mail)
                if input_info:
                    print('')
                    print('Дополнительная информация:')
                    print(input_info)

            elif option2 == 2:
                # print full information
                print(SEPARATOR)
                print('Имя:    ', input_name)
                if 11 <= input_age % 100 <= 19:
                    years = 'лет'
                elif input_age % 10 == 1:
                    years = 'год'
                elif 2 <= input_age % 10 <= 4:
                    years = 'года'
                else:
                    years = 'лет'
                print('Возраст:', input_age, years)
                print('Телефон:', input_phone)
                print('E-mail: ', input_e_mail)
                if input_info:
                    print('')
                    print('Дополнительная информация:')
                    print(input_info)

                # print social links
            else:
                print('Введите корректный пункт меню')
    else:
        print('Введите корректный пункт меню')
