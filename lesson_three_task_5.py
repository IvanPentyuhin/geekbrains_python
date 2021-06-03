'''
Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех случайных слов,
взятых из трёх списков (по одному из каждого):
nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
Например:
get_jokes(2)
["лес завтра зеленый", "город вчера веселый"]
'''

import random

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

def get_jokes(nouns, adverbs, adjectives):
    """Функция возращает шутку"""
    new_jokes = []

    ch_nouns = random.choice(nouns)
    ch_adverbs = random.choice(adverbs)
    ch_adjectives = random.choice(adjectives)
    new_jokes.append(f'{ch_nouns} {ch_adverbs} {ch_adjectives}')

    return new_jokes


print(get_jokes(nouns, adverbs, adjectives))



