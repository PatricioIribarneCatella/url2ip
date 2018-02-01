#!/usr/bin/env python

import socket as s

def get_data():

    print "Type the host name and press 'Enter'\n"
    print "     (For example: google.com)\n"

    return str(raw_input())

def url2ip():

    hostName = get_data()
    ips = s.gethostbyname_ex(hostName)
    
    print ips

if __name__ == '__main__':
    url2ip()
