# Задача 1: Статистика круга
def circle_stats(radius):
    # Проверка: радиус должен быть числом и не быть отрицательным
    if not isinstance(radius, (int, float)) or radius < 0:
        return (0, 0)

    pi_value = 3.14159
    circumference = 2 * pi_value * radius
    area = pi_value * (radius ** 2)
    return (circumference, area)
# Задача 2: Подсчет гласных
def count_vowels(text):
    if not isinstance(text, str):
        return {}
    vowels = 'аеиоуыэюя'
    text = text.lower()

    # Создаем словарь с нулями для всех гласных
    result = {v: 0 for v in vowels}

    for char in text:
        if char in result:
            result[char] += 1

    return result


# Задача 3: Сумма FizzBuzz
def fizzbuzz_sum(n):
    if not isinstance(n, int) or n < 1:
        return 0

    total = 0
    for i in range(1, n + 1):
        # Если число не делится на 3 и не делится на 5
        if i % 3 != 0 and i % 5 != 0:
            total += i
    return total


# Задача 4: Удаление дубликатов и сортировка
def remove_duplicates_sorted(lst):
    if not isinstance(lst, list):
        return []

    unique_list = []
    for item in lst:
        if item not in unique_list:
            unique_list.append(item)

    # Сортировка пузырьком
    n = len(unique_list)
    for i in range(n):
        for j in range(0, n - i - 1):
            if unique_list[j] > unique_list[j + 1]:
                unique_list[j], unique_list[j + 1] = unique_list[j + 1], unique_list[j]

    return unique_list


# Задача 5: Объединение словарей
def merge_dicts(dict1, dict2):
    if not isinstance(dict1, dict) or not isinstance(dict2, dict):
        return {}

    result = dict1.copy()  #копия первого

    for key, value in dict2.items():
        # Если ключ уже есть, складываем значения
        if key in result:
            if isinstance(result[key], (int, float)) and isinstance(value, (int, float)):
                result[key] += value
            else:
                # Если типы не числовые, просто перезаписываем или ставим 0
                result[key] = 0
        else:
            result[key] = value

    return result


# Задача 6: Обработка файла с числами
def process_numbers_file():
    input_file = 'numbers.txt'
    output_file = 'filtered.txt'

    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        filtered_numbers = []
        for line in lines:
            cleaned_line = line.strip()
            # Проверяем, является ли строка числом, включая отрицательные
            if cleaned_line.lstrip('-').isdigit():
                num = int(cleaned_line)
                # Условие: больше 0 и четное
                if num > 0 and num % 2 == 0:
                    filtered_numbers.append(str(num))

        with open(output_file, 'w', encoding='utf-8') as f:
            f.write('\n'.join(filtered_numbers))

        print(f"Готово. Результат записан в {output_file}")

    except FileNotFoundError:
        print(f"Ошибка: Файл {input_file} не найден.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


# Задача 7: Применить функцию к списку
def apply_to_list(func, lst):
    if not isinstance(lst, list) or not callable(func):
        return []

    result = []
    for item in lst:
        try:
            val = func(item)
            result.append(val)
        except Exception:
            result.append(None)
    return result


# Вспомогательная функция
def square_number(x):
    return x * x


# Задача 8: Безопасное деление
def safe_divide(a, b):
    # Проверка на числа
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        return "Ошибка: не числа"

    if b == 0:
        return "Ошибка: деление на ноль"

    return a / b


# Задача 9: -
def process_students_csv():
    print("-")
# Задача 10: Анализатор текста
def text_analyzer(text):
    if not isinstance(text, str):
        # Возвращаем пустую структуру
        return {'char_count': 0,
                'word_count': 0,
                'sentence_count': 0,
                'most_common_word': ''}

    char_count = len(text)

    # Подсчет предложений по знакам препинания
    sentence_count = 0
    for char in text:
        if char in '.!?':
            sentence_count += 1

    # Очистка текста от пунктуации для подсчета слов
    translator = str.maketrans('', '', string.punctuation)
    clean_text = text.translate(translator).lower()

    words = clean_text.split()
    word_count = len(words)

    # Поиск самого часто встречаемого слова
    most_common_word = ''
    if words:
        freq_dict = {}
        for word in words:
            freq_dict[word] = freq_dict.get(word, 0) + 1

        # Находим слово с максимальной частотой
        max_count = 0
        for word, count in freq_dict.items():
            if count > max_count:
                max_count = count
                most_common_word = word

    return {
        'char_count': char_count,
        'word_count': word_count,
        'sentence_count': sentence_count,
        'most_common_word': most_common_word
    }


def menu():
    while True:
        print("\nВыберите задания на проверку (от 1 до 10, 0 выход)")

        choice = input("Выберите номер задания: ")

        if choice == '0':
            print("Выход из программы.")
            break

        elif choice == '1':
            try:
                r = float(input("Введите радиус круга: "))
                circ, area = circle_stats(r)
                print(f"Длина окружности: {circ:.2f}, Площадь: {area:.2f}")
            except ValueError:
                print("Ошибка: введите числовое значение.")

        elif choice == '2':
            s = input("Введите строку для поиска гласных: ")
            print(f"Результат: {count_vowels(s)}")

        elif choice == '3':
            try:
                n = int(input("Введите предел N для FizzBuzz: "))
                print(f"Сумма чисел: {fizzbuzz_sum(n)}")
            except ValueError:
                print("Ошибка: введите целое число.")

        elif choice == '4':
            raw_input = input("Введите элементы списка через пробел: ")
            # Пытаемся преобразовать в числа, если возможно
            test_list = []
            for item in raw_input.split():
                try:
                    test_list.append(float(item) if '.' in item else int(item))
                except ValueError:
                    test_list.append(item)
            print(f"Результат обработки: {remove_duplicates_sorted(test_list)}")

        elif choice == '5':
            print("Введите элементы первого словаря (формат ключ:значение через пробел, напр. a:10 b:20):")

            def parse_to_dict(text):
                d = {}
                for pair in text.split():
                    if ':' in pair:
                        k, v = pair.split(':', 1)
                        try:
                            d[k] = float(v)
                        except ValueError:
                            d[k] = v
                return d

            d1 = parse_to_dict(input("Словарь 1: "))
            d2 = parse_to_dict(input("Словарь 2: "))
            print(f"Результат слияния: {merge_dicts(d1, d2)}")

        elif choice == '6':
            process_numbers_file()

        elif choice == '7':
            raw_input = input("Введите числа через пробел для возведения в квадрат: ")
            test_list = []
            for item in raw_input.split():
                try:
                    test_list.append(float(item))
                except ValueError:
                    test_list.append(item)  # Добавляем как строку для проверки обработки ошибок
            print(f"Результат (квадраты): {apply_to_list(square_number, test_list)}")

        elif choice == '8':
            try:
                a = float(input("Введите делимое (A): "))
                b = float(input("Введите делитель (B): "))
                print(f"Результат: {safe_divide(a, b)}")
            except ValueError:
                print("Ошибка: нужно вводить числа.")

        elif choice == '9':
            process_students_csv()

        elif choice == '10':
            text = input("Введите текст для полного анализа: ")
            stats = text_analyzer(text)
            print("\n--- ОТЧЕТ ---")
            print(f"Символов: {stats['char_count']}")
            print(f"Слов: {stats['word_count']}")
            print(f"Предложений: {stats['sentence_count']}")
            print(f"Частое слово: '{stats['most_common_word']}'")

        else:
            print("Неверный ввод. Пожалуйста, выберите число от 0 до10.")

if __name__ == '__main__':
    menu()
