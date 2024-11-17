def single_root_words(root_word, *other_words):
    same_words = []
    for i in other_words:
        if i.count(root_word):
            same_words.append(i)
    # return same_words
    for i in other_words:
        root_word = root_word.lower()
        if root_word.count(i.lower()):
            same_words.append(i)
    return same_words


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)



# 1. Объявите функцию single_root_words и напишите в ней параметры root_word и *other_words.
# 2.  Создайте внутри функции пустой список same_words, который пополнится нужными словами.
# 3. При помощи цикла for переберите предполагаемо подходящие слова.
# 4.Пропишите корректное относительно задачи условие, при котором добавляются слова в результирующий список same_words.
# 5. После цикла верните образованный функцией список same_words.
# 6.  Вызовите функцию single_root_words и выведете на экран(консоль) возвращённое ей значение.
# 7.  Пример результата выполнения программы:

