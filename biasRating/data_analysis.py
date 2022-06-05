"""
File: data_analysis.py
----------------------
This program read in data on cumulative infections of a disease
in different locations, and computes the number of infections
per day at each location.
"""


def load_data(filename):
    """
    The function takes in the name of a datafile (string), which
    contains data on locations and their seven day cumulative number
    of infections.  The function returns a dictionary in which the
    keys are the locations in the data file, and the value associated
    with each key is a list of the (integer) values presenting the
    cumulative number of infections at that location.
    >>> load_data('data/disease1.txt')
    {'Evermore': [1, 1, 1, 1, 1, 1, 1], 'Vanguard City': [1, 2, 3, 4, 5, 6, 7], 'Excelsior': [1, 1, 2, 3, 5, 8, 13]}
    """
    result = {}
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            parts = line.split(",")
            city = parts[0]
            city = city.strip()
            data = []
            for i in range(1, len(parts)):
                data.append(int(parts[i]))
            result[city] = data
    return result


def daily_cases(cumulative):
    """
    The function takes in a dictionary of the type produced by the load_data
    function (i.e., keys are locations and values are lists of seven values
    representing cumulative infection numbers).  The function returns a
    dictionary in which the keys are the same locations in the dictionary
    passed in, but the value associated with each key is a list of the
    seven values (integers) presenting the number of new infections each
    day at that location.
    >>> daily_cases({'Test': [1, 2, 3, 4, 4, 4, 4]})
    {'Test': [1, 1, 1, 1, 0, 0, 0]}
    >>> daily_cases({'Evermore': [1, 1, 1, 1, 1, 1, 1], 'Vanguard City': [1, 2, 3, 4, 5, 6, 7], 'Excelsior': [1, 1, 2, 3, 5, 8, 13]})
    {'Evermore': [1, 0, 0, 0, 0, 0, 0], 'Vanguard City': [1, 1, 1, 1, 1, 1, 1], 'Excelsior': [1, 0, 1, 1, 2, 3, 5]}
    """
    result = {}
    for key in cumulative:
        raw = cumulative.get(key)
        new = [raw[0]]
        for i in range(1, len(raw)):
            delta = raw[i] - raw[i-1]
            new.append(delta)
        result[key] = new
    return result


def main():
    filename = 'data/disease1.txt'

    data = load_data(filename)
    print(f"Loaded datafile {filename}:")
    print(data)

    print("Daily infections: ")
    print(daily_cases(data))


if __name__ == '__main__':
    main()
