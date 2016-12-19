import sys

# f :: String -> Int
# g :: Int -> String

# f . g


def validate_expression(input):
    definitions = {}

    for line in input:
        if line != '\n':
            name = line.split(' :: ')[0]
            param = line.split(' :: ')[1].split(' -> ')[0]
            ret_type = line.split(' :: ')[1].split(' -> ')[1][:-1]
            definitions[name] = (param, ret_type)
        else:
            break

    input[-1] = input[-1].strip('\n')
    comp = input[-1].split(' . ')

    replaced = []
    for func in comp[::-1]:
        replaced.append(definitions[func][0])
        replaced.append(definitions[func][1])

    del replaced[0]
    replaced.pop()

    replaced = replaced[::-1]

    while replaced != []:
        t = replaced[-1]
        replaced.pop()
        t1 = replaced[-1]
        replaced.pop()
        if t != t1:
            return False

    return True


def main():
    inpt = list(sys.stdin)
    print(validate_expression(inpt))


if __name__ == '__main__':
    main()
