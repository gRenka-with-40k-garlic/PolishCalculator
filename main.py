#(9+12)-10*(40-20)
#вывода нет, ввода нет, да и я не знаю правильно ли написала
#я пару часов сидела на шарпах писала, но чет решила попробовать на пайтоне и тут хотябы работает

def ReversePolishNotation(str):
    elements = Parse(str)
    str2 = []
    resultstr = []
    operands = ["+", "-", "*", "/", "(", ")"]
    for element in elements:
        if element == "(":
            str2 = [element] + str2
        elif element in operands:
            if str2 == []:
                str2 = [element]
            elif element == ")":
                while (True):
                    q = str2[0]
                    str2 = str2[1:]
                    if q == "(":
                        break
                    resultstr += [q]
            elif Priority(str2[0]) < Priority(element):
                str2 = [element] + str2
            else:
                while (True):
                    if str2 == []:
                        break
                    q = str2[0]
                    resultstr += [q]
                    str2 = str2[1:]
                    if Priority(q) == Priority(element):
                        break
                str2 = [element] + str2
        else:
            resultstr += [element]
    while (str2 != []):
        q = str2[0]
        resultstr += [q]
        str2 = str2[1:]
    return resultstr


def Priority(o):
    if o == "+" or o == "-":
        return 1
    elif o == "*" or o == "/":
        return 2
    elif o == "(":
        return 0


def Parse(str):
    delims = ["+", "-", "*", "/", "(", ")"]
    elements = []
    tmp = ""
    for i in str:
        if i != " ":
            if i in delims:
                if tmp != "":
                    elements += [tmp]
                elements += [i]
                tmp = ""
            else:
                tmp += i
    if tmp != "":
        elements += [tmp]
    return elements

print(ReversePolishNotation("(9+12)-10*(40-20)"))