from data_create import name_data, sername_data, phone_data, adress_data
def input_data():
    name = name_data()
    surname = sername_data()
    phone = phone_data()
    adress = adress_data()
    var = int(input(f"В каком формате записать данные \n\n"
    f"1 Вариант: \n{name}\n{surname}\n{phone}\n{adress}\n"
    f"2 Вариант: \n {name};{surname};{phone};{adress} \n"
    f"Выберите вариант: "))

    while var !=1 and var != 2:
        print("Неправильный ввод")
        var = int(input('Выберите вариант: '))
    
    if var == 1:
        with open('data_first_variant.csv', 'a', encoding='utf-8') as f:
            f.write(f"{name}\n{surname}\n{phone}\n{adress}\n\n")
    elif var == 2:
        with open('data_second_variant.csv', 'a', encoding='utf-8') as f:
            f.write(f"{name};{surname};{phone};{adress} \n \n")

def print_data():
    print('Вывожу данные из первого файла: \n')
    with open('data_first_variant.csv', 'r', encoding='utf-8') as f:
        data_first = f.readlines()
        data_first_list = []
        j = 0
        for i in range (len(data_first)):
            if data_first[i] == '\n' or i == len(data_first) - 1:
                data_first_list.append(''.join(data_first[j: i + 1]))
                j = i
        print(''.join(data_first_list))
    print('Вывожу данные из второго файла: \n')
    with open('data_second_variant.csv', 'r', encoding='utf-8') as f:
        data_second = f.readlines()
        print(*data_second)


def change_data():

    var = int(input(f"В каком формате у вас была запись данных? \n\n"
    f"1 Вариант: \n name\n surname \n phone\n adress \n"
    f"2 Вариант: \n name;surname;phone;adress \n"
    f"Выберите вариант: "))

    while var !=1 and var != 2:
        print("Неправильный ввод")
        var = int(input('Выберите вариант: '))

    if var == 1:
        with open ('data_first_variant.csv', 'r') as f:
            old_data = f.read()
        old_text = input('Введите старый текст: ')
        temp = False

        while(temp == False):
            if (old_text in old_data):
                print("Запись найдена! \n")
                temp = True
            else:
                print("К сожалению Запись не найдена попробуйте снова")
                old_text = input('Введите старый текст: ')
        
        new_data = old_data.replace(old_text, input('Введите новый текст: '))
        with open ('data_first_variant.csv', 'w') as f:
            f.write(new_data)

    if var == 2:
        with open ('data_second_variant.csv', 'r') as f:
            old_data = f.read()
        old_text = input('Введите старый текст: ')
        temp = False

        while(temp == False):
            if (old_text in old_data):
                print("Запись найдена! \n")
                temp = True
            else:
                print("К сожалению Запись не найдена попробуйте снова")
                old_text = input('Введите старый текст: ')

        new_data = old_data.replace(old_text, input('Введите новый текст: '))

        with open ('data_second_variant.csv', 'w') as f:
            f.write(new_data)

def dalate_data():
    var = int(input(f"В каком формате у вас была запись данных? \n\n"
    f"1 Вариант: \n name\n surname \n phone\n adress \n"
    f"2 Вариант: \n name;surname;phone;adress \n"
    f"Выберите вариант: "))

    while var !=1 and var != 2:
        print("Неправильный ввод")
        var = int(input('Выберите вариант: '))

    if var == 1:
        with open ('data_first_variant.csv', 'r') as f:
            old_data = f.read()
        old_text = input('Введите старый текст, который хотите удалить: ')
        temp = False
        delete = ''

        while(temp == False):
            if (old_text in old_data):
                print("Запись найдена! \nУдаление произошло успешно! \n")
                temp = True
            else:
                print("К сожалению Запись не найдена попробуйте снова")
                old_text = input('Введите старый текст: ')
        
        new_data = old_data.replace(old_text, delete)
        with open ('data_first_variant.csv', 'w') as f:
            f.write(new_data)

    if var == 2:
        with open ('data_second_variant.csv', 'r') as f:
            old_data = f.read()
        old_text = input('Введите старый текст: ')
        temp = False
        delete = ''

        while(temp == False):
            if (old_text in old_data):
                print("Запись найдена! \nУдаление произошло успешно! \n")
                temp = True
            else:
                print("К сожалению Запись не найдена попробуйте снова")
                old_text = input('Введите старый текст: ')

        new_data = old_data.replace(old_text, delete)

        with open ('data_second_variant.csv', 'w') as f:
            f.write(new_data)
