from functools import wraps
from datetime import datetime
from time import time
from time import sleep


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


def log(filename):
    def accepter(func):
        @wraps(func)
        def decorator(*args, **kwargs):
            with open(filename, 'a') as f:
                f.write("{} was called at {}\n".format(func.__name__,
                                                       datetime.now()))
            return func(*args, **kwargs)
        return decorator
    return accepter


@log('log.txt')
@encrypt(2)
def get_low(a):
    return "Get get get low" * a


def performance(filename):
    def accepter(func):
        @wraps(func)
        def decorator(*args, **kwargs):
            start_time = time()
            res = func(*args, **kwargs)
            end_time = time()
            with open(filename, 'a') as f:
                f.write("{} was called and took {} seconds to complete.\n"
                        .format(func.__name__, end_time - start_time))
            return func(*args, **kwargs)
        return decorator
    return accepter


@performance('logp.txt')
def something_heavy():
    sleep(2)
    return "I am done!"


def main():
    print(get_low(1))
    print(something_heavy())


if __name__ == '__main__':
    main()
