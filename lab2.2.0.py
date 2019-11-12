"""
Використовуючи алгоритм Евкліда, знайти НСД двох чисел.
"""
flag = ""
while flag == "":
    def T():
        while True:
            try:
                x = int(input())
                y = int(input())
                if x <= 0 or y <= 0:
                    print("Not real")
                else:
                    while x != 0 and y != 0:
                        if x > y:
                            x = x % y
                        else:
                            y = y % x
                    print(x + y)
                return x
            except:
                print("Try again!!!")


    print("enter:")
    T()
    print(" if you want to continue : put ENTER , if not : write SOMETHING + ENTER ")
    flag = input()
