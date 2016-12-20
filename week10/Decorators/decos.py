def accepts(*args):
    type_lst = args

    def accepter(func):
        def check_types(*args):
            for arg in range(len(args)):
                if type(args[arg]) != type_lst[arg]:
                    raise TypeError("Argument {} of say_hello is not {}"
                                    .format(arg + 1, type_lst[arg]))
            return func(*args)
        return check_types
    return accepter


@accepts(str, int)
def say_hello(name, money):
    return "Hello, I am {}".format(name)


def encrypt(key):

    def accepter(func):
        def encrypter():
            res = func()
            res = list(res)
            for sym in range(len(res)):
                if res[sym] != ' ':
                    res[sym] = chr(ord(res[sym]) + key % 26)
            return ''.join(res)
        return encrypter
    return accepter


@encrypt(2)
def get_low():
    return "Get get get low"


def main():
    print(get_low())


if __name__ == '__main__':
    main()
