# Алгоритм Боєра-Мура
def boyer_moore_search(text, pattern):
    def bad_char_table(pattern):
        table = {}
        for i in range(len(pattern)):
            table[pattern[i]] = i
        return table

    bad_char = bad_char_table(pattern)
    m = len(pattern)
    n = len(text)
    s = 0

    while s <= n - m:
        j = m - 1
        while j >= 0 and pattern[j] == text[s + j]:
            j -= 1
        if j < 0:
            return s
        else:
            s += max(1, j - bad_char.get(text[s + j], -1))
    return -1
