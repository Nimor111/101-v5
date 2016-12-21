from functools import wraps


def accepts(*types, **kwargs):

    def accepter(func):
        @wraps(func)
        def decorator(*args, **kwargs):
            for arg in range(len(args)):
                if type(args[arg]) != types[arg]:
                    raise TypeError("Argument {} of say_hello is not {}"
                                    .format(arg + 1, types[arg]))
            return func(*args, **kwargs)
        return decorator
    return accepter


@accepts(str, int)
def say_hello(name, money):
    return "Hello, I am {}".format(name)


def encode(string, key):
    string = list(string)
    for sym in range(len(string)):
        if string[sym] != ' ':
            string[sym] = chr(ord(string[sym]) + key % 26)
    return ''.join(string)


def encrypt(key):

    def accepter(func):
        @wraps(func)
        def decorator(*args, **kwargs):
            res = func(*args, **kwargs)
            return encode(res, key)
        return decorator
    return accepter


@encrypt(2)
def get_low(a):
    return "Get get get low" * a


def main():
    print(get_low(1))


if __name__ == '__main__':
    main()
