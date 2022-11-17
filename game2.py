"Number queez"

import numpy as np

def random_predict(number: int=1) -> int:
    """автоматическое угадывание числа компьютером
        Args: number (int, optional) загаданное число defaults: 1
        int- число попыток
    """
    count=0
    
    while True:
        count +=1
        predict_number = np.random.randint(1,101) # генерирует рандомное число
        if number == predict_number:
            break
    return(count)
def score_game(random_predict) -> int:
    """за какое количество попыток в среднем угадывается число

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: количество попыток
    """
    count_ls= []
    np.random.seed(1) #фиксируем сид для воспроизводимости
    random_array= np.random.randint(1,101, size = [1000]) # список чисел
    for number in random_array:
        count_ls.append(random_predict(number))
    score = int(np.mean(count_ls))
    print(f'Ваш алгоритм угадывает число в среднем за {score} попытки')
    return(score)

if __name__ == '__main__':
    score_game(random_predict)
      
