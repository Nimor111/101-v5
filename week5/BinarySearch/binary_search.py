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


def find_turning_point(xs, start, end):

    middle = (start + end) // 2
    left = middle - 1
    right = middle + 1

    if end - start < 2:
        if xs[end] < xs[end - 1]:
            return "Turning point is {} on index {}.".format(xs[end], end)
        return False

    if xs[left] > xs[middle]:
        return "Turning point is {} on index {}." \
            .format(xs[middle], middle)

    if xs[left] < xs[middle]:
        in_left = find_turning_point(xs, start, middle)
        if in_left:
            return in_left
        elif xs[middle] > xs[right]:
            if middle == end - 1:
                return "Turning point is {} on index {}." \
                    .format(xs[middle + 1], middle + 1)
            return "Turning point is {} on index {}." \
                .format(xs[middle], middle)
        else:
            return find_turning_point(xs, right, end)

        # else:
        #     in_left = find_turning_point(xs, start, middle)
        #     print("INLEFT IS FUCKING: ", in_left)
        #     if in_left:
        #         print("returning in left")
        #         return in_left
        #     else:
        #         print("Ever get here?")
        #         return find_turning_point(xs, right, end)


def main():
    print(binary_search([1], 0, 1, 1))


if __name__ == '__main__':
    main()
