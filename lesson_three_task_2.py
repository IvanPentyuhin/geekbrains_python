'''
*(вместо задачи 1) Доработать предыдущую функцию в num_translate_adv(): реализовать корректную работу с числительными,
начинающимися с заглавной буквы — результат тоже должен быть с заглавной. Например:
num_translate_adv("One")
"Один"
num_translate_adv("two")
"два"
'''



eng_rus = {'zero': 'ноль',
           'one': 'один',
           'two': 'два',
           'three': 'три',
           'four': 'четыре',
           'five': 'пять',
           'six': 'шесть',
           'seven': 'семь',
           'eight': 'восемь',
           'nine': 'девять',
           'ten': 'десять'}




def num_translate_adv(user_numb):

    if user_numb.istitle():
        user_lower = user_numb.lower()
        if user_lower in eng_rus.keys():
            for key in eng_rus.keys():
                if user_lower == key:
                    print(eng_rus[key].title())
        else:
            print(None)
    else:
        if user_numb in eng_rus.keys():
            for key in eng_rus.keys():
                if user_numb == key:
                    print(eng_rus[key].lower())
        else:
            print(None)

user_numb = input('Введите число от 0 до 10 словом на английском языке: ')

num_translate_adv(user_numb)