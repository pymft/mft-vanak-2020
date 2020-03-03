def decorator_creator(color):
    colors_map = {'red': '31', 'blue': '34', 'yellow': '33'}

    def color_function(f):
        def inner(x):
            out = "\033[" + colors_map[color] + "m"
            out = out + str(f(x))
            out = out + "\033[0m"
            return out

        return inner

    return color_function


def twice(f):
    def inner(x):
        out = f(x)
        out = out * 2
        return out

    return inner


@decorator_creator('yellow')
def echo(s):
    return s

@decorator_creator('yellow')
def factorial(n: int):
    answer = 1
    for i in range(1, n+1):
        answer = answer * i

    return answer

print(factorial(10))
