# -*- coding: utf-8 -*-
import os

print(os)
sec = [30, 15, 15, 30, 30, 15, 15, 30, 30, 15, 15, 30, 30, 15, 15, 30]
sen = ["1/2", "√2/2", "√3/2", "1", "√3/2", "√2/2", "1/2", "0", "-1/2", "-√2/2", "-√3/2", "-1", "-√3/2", "-√2/2", "-1/2",
       "0"]
cos = ["√3/2", "√2/2", "1/2", "0", "-1/2", "-√2/2", "-√3/2", "-1", "-√3/2", "-√2/2", "-1/2", "0", "1/2", "√2/2", "√3/2",
       "1"]
tan = ["√3/3", "1", "√3", "INDEFINIDO!", "-√3", "-1", "-√3/3", "0", "√3/3", "1", "√3", "INDEFINIDO!", "-√3", "-1",
       "-√3/3", "0"]
graus = 0
base = 180
needle = 0
needle1 = 0
pSen = 0
pCos = 0
pTan = 0
loop = "y"


def to_radian(until, num1, num2):
    for i in range(until + 1):
        if i != 0:
            r1 = num1 % i
            r2 = num2 % i
            if r1 == 0 and r2 == 0:
                rad1 = int(num1 / i)
                rad2 = int(num2 / i)
                div = i
    return [div, rad1, rad2]


def format_pi(val1, val2):
    if val1 == 1 and val2 > 1:
        r = 'π/' + str(val2)
    elif val1 == 1 and val2 == 1:
        r = 'π'
    elif val1 > 1 and val2 == 1:
        r = str(val1) + 'π'
    else:
        r = str(val1) + 'π/' + str(val2)
    return r


def anc_wal():
    global sec
    global sen
    global cos
    global tan
    global graus
    global base
    global needle
    global needle1
    global pSen
    global pCos
    global pTan
    op = int(input("How many laps? (0 <> ∞) \n"))
    os.system("clear")
    for i in range(int(16 * op)):
        needle = 0 if needle == 16 else needle
        graus += sec[needle]
        needle1 = 0 if needle1 == 16 else needle1
        pSen = sen[needle1]
        pCos = cos[needle1]
        pTan = tan[needle1]
        needle += 1
        needle1 += 1
        r = to_radian(graus + 1, graus, base)
        pi = format_pi(r[1], r[2])

        output = str(graus) + 'º/' + str(base) + '\n--Div = ' + str(r[0]) + '\n--Rad = ' + str(pi) + '\n--Sen = ' + str(
            pSen) + '\n--Cos = ' + str(pCos) + '\n--Tan = ' + str(pTan) + '\n'
        print(output)


def anc_otl():
    global sec
    global sen
    global cos
    global tan
    global graus
    global base
    global needle
    global needle1
    global pSen
    global pCos
    global pTan
    op = int(input("Type the number of lap? (0 <> ∞) \n"))
    graus = op * 360 - 360
    os.system("clear")
    for i in range(int(16 * op)):
        needle = 0 if needle == 16 else needle
        graus += sec[needle]
        needle1 = 0 if needle1 == 16 else needle1
        pSen = sen[needle1]
        pCos = cos[needle1]
        pTan = tan[needle1]
        needle += 1
        needle1 += 1
        r = to_radian(graus + 1, graus, base)
        pi = format_pi(r[1], r[2])

        output = str(graus) + 'º/' + str(base) + '\n--Div = ' + str(r[0]) + '\n--Rad = ' + str(
            pi) + '\n--Sen = ' + str(pSen) + '\n--Cos = ' + str(pCos) + '\n--Tan = ' + str(pTan) + '\n'
        print(output)  # degree to radian


def is_float(val):
    try:
        float(val)
        return True
    except:
        return False


# Coversion_degree_to_radian
def c_dinr():
    os.system('clear')
    print("You selected conversion of degree to radian.")
    op = "y"
    while op == "y":
        v = True
        while v == True:
            degree = input("Type the value of degree: ")
            if is_float(degree) == True:
                v = False
            else:
                print("Type just number integer or number decimal!")
        c = to_radian(int(degree), float(degree), 180)
        pi = format_pi(c[1], c[2])
        print(str(degree) + '|180 /' + str(c[0]) + ' = ' + pi + '\n')
        v = True
        while v == True:
            op = input("Do you want a new calculation? (Y/N) \nAnswer: ")
            if op == 'Y' or op == 'y':
                v = False
                pass
            elif op == 'N' or op == 'n':
                v = False
                op = 'n'
            else:
                print("Y = YES and N = NO")


def prepare_pi(string):
    p = string.split('/')
    p[0] = p[0].slit('pi')
    return [p[0][0], p[1]]


# radian to degree
def c_rind():
    os.system("clear")
    print("You selected conversion of radians to degree")
    op = "y"
    while op == "y":
        radian = prepare_pi(input('Type the value ex: "2pi/3 or pi/3  or pi" of radian: '))
        c = 180 * radian[0] / radian[1]
        print("180x" + str(radian[0]) + "/" + str(radian[1]) + " = " + str(c))



        v = True
        while v == True:
            op = input("Do you want a new calculation? (Y/N) \nAnswer: ")
            if op == 'Y' or op == 'y':
                v = False
                pass
            elif op == 'N' or op == 'n':
                v = False
                op = 'n'
            else:
                print("Y = YES and N = NO")

def decision():
    r = ""
    loop = 1
    while loop == 1:
        usOp = input("Go back to menu? (Y/N)")
        if usOp == "Y" or usOp == "y":
            r = "y"
            loop = 0
        elif usOp == "N" or usOp == "n":
            print("Ok...\nTo the next.")
            r = "n"
            loop = 0
        else:
            print("Answer unknown!\n")
    return r


while loop == "y":
    os.system('clear')
    print("math-CDR (Conversion of degree and radian) v1.0\n\n")
    case = input("What do you want?\n"
                 "[1] Angles notable in circumference from 1 until ∞. (With all laps)\n"
                 "[2] Angles notable in circumference from 1 until ∞. (Only the lap!)\n"
                 "[3] Conversion of degree to radian.\n"
                 "[4] Conversion of radian to degree.\n"
                 "[0] Exit\n\nAnswer: ")

    # definir_funções
    if case.isdigit() != True:
        os.system('clear')
        print("Answer unknown. Type only numbers from 0 until 4!\n")
    elif int(case) == 0:
        print("math-CDR closed!")
        loop = "n"
    elif int(case) == 1:
        anc_wal()
        loop = decision()
    elif int(case) == 2:
        anc_otl()
        loop = decision()
    elif int(case) == 3:
        c_dinr()
    elif int(case) == 4:
        c_rind()
        loop = decision()
    else:
        print(float(case))
        os.system('clear')
        print("Answer unknown!\n")
