import json


def get_data(filename):
    with open(filename, 'r') as f:
        data = json.load(f)

    return data


def filter_names(data):
    new_data = {}
    for key in data.keys():
        pass


def main():
    data = get_data('stat.json')


if __name__ == '__main__':
    main()
