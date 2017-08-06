# /usr/local/Cellar/python3/3.6.2

def sort(input):
    if not isinstance(input, list):
        return []

    return input


def whoIsBigger(a, b):
    if a > b:
        return a
    else:
        return b

def whoissmaller(a, b):
    if b < a:
        return b
    else:
        return a

def equal(a, b):
    return a + b

def equal3number(a,b,c):
    return a + b + c

def times4number(a,b,c,d):
    return a * b * c * d

def divide(number1, number2):
    if number2 == 0:
        return number1

    return number1 / number2

if __name__ == '__main__':
    # print("this is my project")
    input = [0, 1, 11, 2, 13, 15, 1, 6, 5]
    output = sort(input)
    print(output)

    c = 19
    d = 10

    print(whoIsBigger(c, d))

    print(whoIsBigger(200, 199))

    print(whoissmaller(200, 199))

    print(equal(200, 199))

    print(equal(555555,8888))

    print(equal(12345,6789))

    print(equal(99987458748957895782978,494902020302090))

    print(equal3number(574875827492379,8745878,3839229009911))

    print(times4number(859498378492798,10101289837293728,182100190100298347,102476388861021001))

    print(divide(10, 2))

    print(divide(574875092849894823904829048089, 48392302894989202))