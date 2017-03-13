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
                filterContent(domain)
            else:
                printErrorAndQuit()
        else:
            printErrorAndQuit()
    except Exception as e:
        print( str(e) )
        printErrorAndQuit()

def filterContent(url):
    """ filter .onions """
    INDEX_NAME = "crawling"
    url = "http://localhost:9200/" + INDEX_NAME # URL of the new index
    print('\033[1;30m Test that Elasticsearch is available: %s \033[1;m' % url)

def printErrorAndQuit():
    """Printing the usage information"""
    print("Filters an onion domain from the index.\n")
    print("Usage: ./filter.py somesite0128dj2.onion")
    print("Example: ./filter.py msydqstlz2kzerdg.onion\n")
    sys.exit()

if __name__ == '__main__':
    main()
