"""
Три опору R1, R2, R3 з'єднані паралельно. Знайти опір з'єднання. Величина опорів вводиться користувачем.
"""
flag = ""
while flag == "":

    try:
        a = int(input('Enter expecting number of resistors:'))
        Temporary_list = []
        n = 0
        while a > n:
            b = float(input('Resistor resistance:'))
            if b >= 0:
                Temporary_list.append(1 / b)
                n += 1
            else:
                print(False)
        Equation = 1 / sum(Temporary_list)
        print(Equation)
    except:
        print(False)
    flag = input(" if you want to continue : put ENTER , if not : write SOMETHING + ENTER:")
