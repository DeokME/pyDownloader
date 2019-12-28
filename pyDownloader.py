#!/usr/bin/python

import sys
import urllib

# Arguments : Download URL, Download Dest

'''
./pyDownloader.py 'http://example.com/test/example.pdf' /test/test.pdf
'''

print 'Argument List:', str(sys.argv)

if len(sys.argv) < 2:
    print 'Wrong number of args'
else:
    print 'URL : ', str(sys.argv[1])
    print 'Dest : ', str(sys.argv[2])

    url = sys.argv[1]
    dest = sys.argv[2]

    testfile = urllib.URLopener()
    testfile.retrieve(url, dest)