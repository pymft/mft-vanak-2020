import time


def say_hello(f):
    def inner(s):

        time.sleep(1)

        out = f(s)

        return out
    return inner


@say_hello
def echo(s: str):
    print(s)


echo("salam")
echo("salam")