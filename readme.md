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

### Результати

#### Пошук існуючого підрядка:

- **Boyer-Moore Search:** `0.000571 секунд` — Найшвидший алгоритм для пошуку існуючого підрядка.
- **Rabin-Karp Search:** `0.000843 секунд` — Другий за швидкістю, порівнює хеші підрядків.
- **KMP Search:** `0.001066 секунд` — Найповільніший для існуючого підрядка, хоча все ще доволі швидкий.

#### Пошук неіснуючого підрядка:

- **Boyer-Moore Search:** `0.033315 секунд` — Найшвидший при пошуку неіснуючого підрядка.
- **KMP Search:** `0.256788 секунд` — Помітно повільніший через необхідність перевірки більшої кількості символів.
- **Rabin-Karp Search:** `0.276345 секунд` — Найповільніший, оскільки перевіряє хеші кожної частини тексту.

### Загальний висновок:

- **Алгоритм Боєра-Мура** показав найкращі результати як для пошуку існуючих, так і неіснуючих підрядків.
- **Алгоритм Рабіна-Карпа** є ефективним для існуючих підрядків, але значно повільнішим для неіснуючих.
- **Алгоритм Кнута-Морріса-Пратта** працює доволі швидко для існуючих підрядків, але в порівнянні з Боєра-Мура для пошуку неіснуючих підрядків він значно повільніший.

## Використання

Для запуску тестування ви можете використати наступні команди:

```bash
python3 task03.py
