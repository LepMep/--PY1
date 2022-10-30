def get_count_char(str_):
    new_str = str_.lower()
    empty_dic = {}
    DEFAULT_NUMBER = 0
    for symbol in new_str:
        if symbol.isalpha():
            empty_dic[symbol] = empty_dic.get(symbol, DEFAULT_NUMBER) + 1

    return empty_dic

def percentage_of_symbols(dictionary):
    percentage = {}
    for key in dictionary.keys():
       percentage[key] = round(dictionary.get(key) / sum(dictionary.values()) * 100, 2)

    return percentage

main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))
print(percentage_of_symbols(get_count_char(main_str)))
