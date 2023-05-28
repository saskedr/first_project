meme_dict = {
            "КРИНЖ": "Что-то очень странное или стыдное",
            "ЛОЛ": "Что-то очень смешное",
            "РОФЛ": "Шутка"
            }

# log
# log
# log
# log
# log
# log
# log
            
word = input("Введите непонятное слово: ").upper()

if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print('Упс-с-с, такого слова и я не знаю ;c')
