import re


def reduce_file_path(path):
    new_path = path.split("/")[::-1]
    res_path = []
    path_iter = iter(new_path)
    for el in path_iter:
        if el == ".":
            pass
        elif el == "..":
            next(path_iter)
        else:
            res_path.append(el)
    if len(res_path) == 1:
        res_path.append("")
    res_path = list(re.sub(r'(/)\1+', r'\1', "/".join(res_path[::-1])))

    if res_path[len(res_path) - 1] == "/" and len(res_path) > 1:
        del res_path[len(res_path) - 1]

    return "".join(res_path)
