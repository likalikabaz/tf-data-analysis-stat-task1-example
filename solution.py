import numpy as np

chat_id = 753540521 
# https://shitpoet.cc/sshots/2023-04-07--193056--196905498.png
def solution(x: np.array) -> float:
    offset = 791
    i = 0
    while i < len(x):
        x[i] = x[i] - offset
        i = i + 1
    # a_x - expected value of `x`, average over `x`
    sum = 0
    i = 0
    while i < len(x):
        sum = sum + x[i]
        i = i + 1
    average_x = sum / len(x)
    
    i = 0
    y = []
    while i < len(x):
        y.append(x[i] - average_x)
        i = i + 1
    i = 0    
    while i < len(y):
        y[i] = y[i] * y[i]
        i = i + 1
    sum = 0    
    i = 0
    while i < len(y):
        sum = sum + y[i]
        i = i + 1
        
    variance_x = sum / len(y)
    
    # print(x)
    # print(average_x)
    # print(variance_x)
    # print(y)
    
    average = math.log((average_x ** 2) / math.sqrt(average_x ** 2 + variance_x ** 2))

    return average # Ваш ответ
