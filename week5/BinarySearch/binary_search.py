# binary sort in python3
# author - Georgi Bojinov, Hack Bulgaria - binary search implementation

def binary_search(xs, start, end, x):
    if x not in xs or x == []:
        return False
    mid = (start + end) // 2
    if x is xs[mid]:
        return mid
    if x < xs[mid]:
        return binary_search(xs, start, mid, x)
    else:
        return binary_search(xs, mid + 1, end, x)


def turning_point(xs, start, end):
    middle = (start + end) // 2
    left = middle - 1

    if end - start < 2:
        return False

    if xs[left] < xs[middle]:
        in_left = turning_point(xs, start, middle)
        if in_left is False:
            return turning_point(xs, middle + 1, end)
        else:
            return in_left
    else:
        return middle


def main():
    print(binary_search([1], 0, 1, 1))


if __name__ == '__main__':
    main()
