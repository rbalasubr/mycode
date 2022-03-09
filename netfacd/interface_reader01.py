#!/usr/bin/env python3
import netifaces
print(netifaces.interfaces())

for i in netifaces.interfaces():
        #print('\n**************Details of Interface - ' + i + ' *********************')
        try:
            print(netifaces.ifaddresses(i)[netifaces.AF_LINK])
            print(netifaces.ifaddresses(i)[netifaces.AF_LINK][0]['addr'])
        except:
            print(netifaces.ifaddresses(i)[netifaces.AF_INET][0]['addr'])

