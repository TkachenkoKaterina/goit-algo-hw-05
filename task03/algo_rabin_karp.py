# Алгоритм Рабіна-Карпа
def rabin_karp_search(text, pattern):
    d = 256  # Кількість символів в алфавіті
    q = 101  # Просте число для обчислення хешів
    m = len(pattern)
    n = len(text)
    h = 1
    p = 0  # Хеш для шаблону
    t = 0  # Хеш для поточного вікна в тексті

    for i in range(m-1):
        h = (h * d) % q

    for i in range(m):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q

    for i in range(n - m + 1):
        if p == t:
            if text[i:i + m] == pattern:
                return i
        if i < n - m:
            t = (d * (t - ord(text[i]) * h) + ord(text[i + m])) % q
            if t < 0:
                t += q
    return -1
