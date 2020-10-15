# D3-4: R solution
words = set()

n = int(input()) # Количество уже сказанных слов

for _ in range(n):
    words.add(input()) # Добавляем считанное слово к множеству уже сказанных слов


new_word = input() # Новое слово - проверочное, нужно ответить на вопрос, было ли оно уже во множестве
# words или нет
if new_word in words:
    print("НЕ ЗАСЧИТНО")
else:
    print("ЗАСЧИТНО")