""" hopefully a quine
"""

import sys


if __name__ == "__main__":
    with open(sys.argv[0], 'r') as file_handler:
        print(file_handler.read())
