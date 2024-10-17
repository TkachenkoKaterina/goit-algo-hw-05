import timeit

# Імпорт алгоритмів
from algo_knuta_morisa_prata import kmp_search
from algo_boyer_moore import boyer_moore_search
from algo_rabin_karp import rabin_karp_search


# Функція для читання файлів
def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()


# Читання статей
article1 = read_file(
    '/Users/kateryna/Documents/GitHub/goit-algo-hw-05/task03/article_1.txt'
    )
article2 = read_file(
    '/Users/kateryna/Documents/GitHub/goit-algo-hw-05/task03/article_2.txt'
    )

# Підрядки
pattern_exist = "Методи та структури даних для реалізації"
pattern_non_exist = "вигаданий приклад"

# Вимірювання часу для існуючого підрядка
time_exist_kmp = timeit.timeit(
    lambda: kmp_search(article1, pattern_exist), number=100
    )
time_exist_bm = timeit.timeit(
    lambda: boyer_moore_search(article1, pattern_exist), number=100
    )
time_exist_rk = timeit.timeit(
    lambda: rabin_karp_search(article1, pattern_exist), number=100
    )

# Вимірювання часу для неіснуючого підрядка
time_non_exist_kmp = timeit.timeit(lambda: kmp_search(
    article1, pattern_non_exist), number=100
    )
time_non_exist_bm = timeit.timeit(
    lambda: boyer_moore_search(article1, pattern_non_exist), number=100
    )
time_non_exist_rk = timeit.timeit(
    lambda: rabin_karp_search(article1, pattern_non_exist), number=100
    )

# Виведення результатів
print(f"KMP Search (existing): {time_exist_kmp} секунд")
print(f"Boyer-Moore Search (existing): {time_exist_bm} секунд")
print(f"Rabin-Karp Search (existing): {time_exist_rk} секунд")

print(f"KMP Search (non-existing): {time_non_exist_kmp} секунд")
print(f"Boyer-Moore Search (non-existing): {time_non_exist_bm} секунд")
print(f"Rabin-Karp Search (non-existing): {time_non_exist_rk} секунд")
