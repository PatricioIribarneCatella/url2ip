#!/usr/bin/env python

import socket as s

def get_data():

    print "Type the host name and press 'Enter'\n"
    print "     (For example: google.com)\n"

    h = str(raw_input())
    print "\n"

    return h

def print_data(hn, al, ipl):

    print "- Host name: " + hn + "\n"

    print "- Alias list"
    print "     (alternative host names, possibly empty)"
    if (len(al)):
        for a in al:
            print a + "\n"
    else:
        print " ---- \n"

    print "- Addresses for the same interface on the same host"
    print "     (often but not always a single address)"
    for ip in ipl:
        print ip + "\n"

def url2ip():

    hn = get_data()

    (hostName, aliasList, ipAddrList) = s.gethostbyname_ex(hn)

    print_data(hostName, aliasList, ipAddrList)

if __name__ == '__main__':
    url2ip()
