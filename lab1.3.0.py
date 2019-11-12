"""
розв'язати систему рівнянь...
"""
flag = "T"
while flag == "T":

    x = float(input())
    a = -x**2-9
    b = (-1)/(x**2+9)
    if x > 13 :
        print(a)
    elif x < 13 :
        print(b)
    else :
        print(a)
        print(b)
    flag = input("T or F")
