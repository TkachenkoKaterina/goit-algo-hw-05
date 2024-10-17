# Порівняння ефективності алгоритмів пошуку підрядків

## Опис проєкту

Цей проєкт містить реалізацію трьох алгоритмів пошуку підрядків у тексті: 
- **Алгоритм Кнута-Морріса-Пратта**
- **Алгоритм Боєра-Мура**
- **Алгоритм Рабіна-Карпа**

Метою проєкту є порівняння швидкості роботи цих алгоритмів на основі двох видів пошуку: 
1. Пошук існуючого підрядка.
2. Пошук неіснуючого підрядка.

## Дані тестування

Для тестування алгоритмів було використано дві статті, завантажені з інтернету, та два типи підрядків:
- Існуючий підрядок: `"Методи та структури даних для реалізації"`
- Неіснуючий підрядок: `"вигаданий приклад"`

Тестування виконувалось із використанням бібліотеки `timeit` для вимірювання часу виконання кожного алгоритму.

# Результати

#### Пошук існуючого підрядка:

- KMP Search (existing): 0.0010660000261850655 секунд
- Boyer-Moore Search (existing): 0.0005713329883292317 секунд
- Rabin-Karp Search (existing): 0.0008426670101471245 секунд

#### Пошук неіснуючого підрядка:

- KMP Search (non-existing): 0.2567880419665016 секунд
- Boyer-Moore Search (non-existing): 0.03331466700183228 секунд
- Rabin-Karp Search (non-existing): 0.2763454159721732 секунд

### Загальний висновок:

- **Алгоритм Боєра-Мура** показав найкращі результати як для пошуку існуючих, так і неіснуючих підрядків.
- **Алгоритм Рабіна-Карпа** є ефективним для існуючих підрядків, але значно повільнішим для неіснуючих.
- **Алгоритм Кнута-Морріса-Пратта** працює доволі швидко для існуючих підрядків, але в порівнянні з Боєра-Мура для пошуку неіснуючих підрядків він значно повільніший.

## Використання

Для запуску тестування ви можете використати наступні команди:

```bash
python3 task03.py
