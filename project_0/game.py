import numpy as np

def guess_number(number: int = 1, n: int = 100) -> int:   
    """За какое количество попыток наш алгоритм угадывает загаданное число

    Args:
        guess_number ([type]): функция угадывания
        number: загаданное число
        n: диапазон загаданного чиса - от 1 до n (по умолчанию до 100)

    Returns:
        int: количество попыток
    """ 
    # задаем диапазон, в котором будем искать загаданное число - range_low, range_high, от 1 до n 
    # первой попыткой count проверяем, является ли загаданное число predict_number верхней границей диапазона n 
    # если первая попытка верна, функция пропустит цикл while и вернет ответ - 1
    predict_number = n
    count = 1
    range_low = 1
    range_high = n  
    # если первая попытка неверна, функция перехдит в цикл while
    # алгоритм сравнивает середину заданного диапазона с загаданным числом, каждый раз уменьшая диапазон поиска
    while predict_number != number:
        predict_number = range_low + (range_high - range_low) // 2 
        count+=1                    
        if predict_number > number:                  
            range_high = predict_number                                           
        elif predict_number < number: 
            range_low = predict_number                                                                  
    return count


def score_game(guess_number) -> int:
    """За какое количество попыток в среднем за 10000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(10000))  # загадали список чисел

    for number in random_array:
        count_ls.append(guess_number(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попытки")
    
print('Run benchmarking for guess_number: ', end='')
score_game(guess_number)  