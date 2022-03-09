#!/usr/bin/env python3
######## EXPLORE READ ##########

myfile = input('Enter name of the file to open: ')
## create file object in "r"ead mode
configfile = open(myfile, "r")

## display file to the screen - .read()
print(configfile.read())

## close file
configfile.close()

######## EXPLORE READLINES ##########
## re-create file object to explore new method
configfile = open("vlanconfig.cfg", "r")

## make a list of file lines - .readlines()
configlist = configfile.readlines()
print(configlist)

## Iterate through configlist
for x in configlist:
    print(x.strip(), end='')
print(len(configlist))

## Always close your file
configfile.close()
