"""
File: extension.py
------------------
beautiful to find URLs from post titles
"""
from googlesearch import search


def find_url(query):
    bbcquery = "bbc " + query
    for j in search(bbcquery, tld='com', num=1, stop=1):
        return j

def main():
    find_url("bbc Yahoo celebrates a decade online")


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
