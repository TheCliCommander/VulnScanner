#!/usr/env python 

import requests

domain = input("enter URL to be scanned: ")
headers = requests.get(domain).headers

if 'X-Frame-Options' in headers:
    print(domain + ' SECURE against clickjack attacks')
else:
    print(domain + ' VULNERABLE to clickjack attacks')

if 'Content-Security-Policy' in headers:
    print(domain + ' SECURE against XSS attacks')
else:
    if 'X-XSS-Protection' in headers:
        print(domain + ' SECURE against XSS attacks')
    else:
        print(domain +' VULNERABLE to XSS attacks')

if 'Strict-Transport-Security' in headers:
    print(domain + ' SECURE SSL/TLS  enforced')
else:
    print(domain + ' VULNERABLE SSL/TLS NOT enforced')
