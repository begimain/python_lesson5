string_1 = "Терпение и труд - все перетрут!"
sub_string_1 = "труд"
string_2 = "Bema"
sep_string_2 = "B,e,m,a"
numlist = ['1', '2', '3']
separator = ', '
character = 'p'
unicode_char = ord(character)
string = "Python is awesome"
new_string = string.center(24)
str = 'xyz\t12345\tabc'
result = str.expandtabs()
random_string = '   this is good '
string_4 = 'This is good  '
string_5 = ' Master of Manicure, '
string_6 = "ThIs ShOuLd Be MiXeD cAsEd."
string_7 = 'BUSINESS LADY'
text = "program is fun"
width = 15

if __name__ == '__main__':
    print(string_1.find(sub_string_1, 3))  # Метод показывает где подстрока находится.
    print(string_1.rfind(sub_string_1, 4))  # Метод возвращает наивысший индекс подстроки.
    print(string_1.index(sub_string_1, 5))  # Метод возвращает индекс подстроки внутри строки.
    print(string_1.rindex(sub_string_1, 6))  # Метод возвращает наивысший индекс подстроки внутри строки.
    print(string_1.replace(sub_string_1, 'пруд'))  # Метод заменяет все вхождения одной строки на другую.
    print(string_2.split(sep_string_2,))  # Метод Разбивает строку на части, и возвращает его списком.
    print(string_1.isdigit())  # Метод указывает на то, состоит ли строка из цифр.
    print(string_2.isalpha())  # Метод указывает на то, состоит ли строка из букв.
    print(string_1.isalnum())  # Метод указывает на то, состоит ли строка из букв и цифр.
    print(string_1.islower())  # Метод указывает на то, состоит ли строка в нижнем регистре.
    print(string_2.isupper())  # Метод указывает на то, состоит ли строка в верхнем регистре.
    print(string_2.isspace())  # Метод указывает на то, состоит ли строка из неотображаемых символов.
    print(string_1.istitle())  # Метод указывает на то, начинаются ли слова в строке с заглавной буквы.
    print(string_2.upper())  # Метод преобразовывает строки к верхнему регистру.
    print(string_1.lower())  # Метод преобразовывает строки к нижнему регистру.
    print(string_1.startswith('терпение'))  # Метод указывает на то, начинается ли строка с указанного префикса.
    print(string_1.endswith('перетрут!'))  # Метод указывает на то, заканчивается ли строка с указаннего префикса.
    print(separator.join(numlist))  # Метод возвращает строку путем объединения всех элементов итератора.
    print(unicode_char)  # Метод  возвращает целое число , представляющее символ Unicode.
    print(chr(97))  # Метод Возвращает символ по его числовому представлению.
    print(string_1.capitalize())  # Метод Переводит первый символ строки в верхний регистр.
    print("Centered String: ", new_string)  # Mетод возвращает строку , проложенные с указанными fillchar.
    print(string_1.count('Т'))  # Метод возвращает количество вхождений подстроки в данной строке.
    print(result)  # Метод возвращает копию строки с пробелами.
    print(random_string.lstrip())  # Метод удалить пробельных символов в начале строки.
    print(string_4.rstrip())  # Метод удалить пробельных символов в конце строки.
    print(string_5.strip())  # Метод удалить пробельных символов в конце и в начале строки.
    print(string_5.partition('of'))  # Метод разбавляет строку на картеж.
    print(string_5.rpartition('of '))  # Метод принимает строковый параметр который отделяет строку от
    # последнего ее появления.
    print(string_6.swapcase())  # Метод переводит символы нижнего регистра в верхний, а верхнего – в нижний.
    print(string_7.title())  # Метод переводит первую букву каждого слова в верхний регистр,
    # а все остальные в нижний.
    print(text.zfill(15))  # Метод возвращает копию строки с добавленными слева символами «0».
    print(text.ljust(width))  # Метод возвращает выровненную по левому краю строку заданной минимальной ширины.
    print(text.rjust(width))  # Метод возвращает выровненную по правому краю строку заданной минимальной ширины.
    print('{name} написал {book}'.format(name = 'Swaroop', book = 'A byte of Python'))  # Иногда бывает нужно
    # составить строку на основе каких-либо данных. Вот здесь-то пригодится метод format.
