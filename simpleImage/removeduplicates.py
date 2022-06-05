"""
File: removeduplicates.py
-------------------------
This program gives you practice with constructing a new list
based on values given to you by the user.  You also get
practice removing duplicates from that list
"""


def read_list():
    result = []
    while True:
        num = int(input("Enter value (0 to stop): "))
        if num == 0:
            break
        result.append(num)
    return result


def remove_duplicates(num_list):
    """
    This function is passed a list of integers and returns a new
    list with all duplicate values from the original list remove.
    >>> remove_duplicates([1, 2, 3, 2, 3, 4])
    [1, 2, 3, 4]
    >>> remove_duplicates([1, 1, 1])
    [1]
    >>> remove_duplicates([])
    []
    """
    result = []
    for num in num_list:
        if num not in result:
            result.append(num)
    return result


def main():
    num_list = read_list()
    print("Original list entered by user: ")
    print(num_list)

    no_duplicates = remove_duplicates(num_list)
    print("List with duplicates removed: ")
    print(no_duplicates)


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
