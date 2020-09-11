def decorator(f):
    def inner(arg: str):
        return "*" + arg + "*"

    return inner


@decorator
def echo(s):
    return s


print(echo("sjfljsdlkfsjdlfsdjflksd"))