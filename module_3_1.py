calls = 0

def count_calls(): # подсчитывающая функция вызовы остальных функций
    global calls
    calls += 1

def string_info(string): # функция принимает аргумент - строку и возвращает кортеж из: длины этой строки, строку в верхнем регистре, строку в нижнем регистре.
    list_ = str(string)
    a = (len(string), string.upper(), string.lower())
    count_calls()
    return a

def is_contains(string, list_to_search): # функция принимает два аргумента: строку и список, и возвращает True, если строка находится в этом списке, False - если отсутствует.
    string = str(string).lower()
    list_to_search = list(list_to_search)
    count_calls()
    for i in range(len(list_to_search)):
        if str(list_to_search[i]).lower() == string:
            a = True
            break
        else:
            a = False
            continue
    return a

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)