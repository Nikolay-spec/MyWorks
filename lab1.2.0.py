"""
Ввести три додатних числа а, b, с. Перевірити, чи будуть вони сторонами трикутника. Якщо так, то обчислити площу цього трикутника.
"""
flag = ""
while flag == "":

    a = float(input())
    b = float(input())
    c = float(input())
    if a < 0 or b < 0 or c < 0 or a + b < c or a + c < b or b + c < a:
        print(False)
    else:
        p = (a + b + c) / 2
        S = (p * (p - a) * (p - b) * (p - c)) ** 0.5
        print(S)
    flag = input("")
