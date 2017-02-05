import json
import matplotlib.pyplot as plt


def get_data(filename):
    '''
    Get the server results from the file
    '''
    with open(filename, 'r') as f:
        data = json.load(f)

    return data


def filter_names(data):
    '''
    Filter names by most frequently encountered servers
    '''
    new_data = {}
    for key in data.keys():
        if (key.startswith('Apache') or 'Apache' in key)\
                and 'Apache' not in new_data.keys():
            new_data['Apache'] = data[key]
        elif key.startswith('Apache') or 'Apache' in key:
            new_data['Apache'] += data[key]
        elif (key.startswith('nginx') or 'nginx' in key)\
                and 'nginx' not in new_data.keys():
            new_data['nginx'] = data[key]
        elif key.startswith('nginx') or 'nginx' in key:
            new_data['nginx'] += data[key]
        elif (key.startswith('Microsoft') or 'Microsoft' in key)\
                and 'Microsoft' not in new_data.keys():
            new_data['Microsoft'] = data[key]
        elif key.startswith('Microsoft') or 'Microsoft' in key:
            new_data['Microsoft'] += data[key]
        elif 'other' not in new_data.keys():
            new_data['other'] = 1
        else:
            new_data['other'] += data[key]
    return new_data


def histogram(data):
    '''
    Make histogram
    '''
    plt.bar(range(len(data)), data.values(), align='center')
    plt.xticks(range(len(data)), data.keys())
    plt.show()


def main():
    data = get_data('stat.json')
    print(filter_names(data))
    histogram(filter_names(data))


if __name__ == '__main__':
    main()
