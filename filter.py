# -*- coding: utf-8 -*-
""" Filter some onions from the index """

import sys
import requests

def main():
    # Read command line arguments
    try:
        if len(sys.argv) == 2:
            domain = str(sys.argv[1])
            if len(domain) == 22:
                #todo : filterContent
            else:
                printErrorAndQuit()
        else:
            printErrorAndQuit()
    except Exception as e:
        print( str(e) )
        printErrorAndQuit()

def printErrorAndQuit():
    """Printing the usage information"""
    print("Filters an onion domain from the index.\n")
    print("Usage: ./filter.py some.onion")
    print("Example: ./filter.py msydqstlz2kzerdg.onion\n")
    sys.exit()

if __name__ == '__main__':
    main()
