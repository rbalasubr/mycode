# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 21:21:47 2022

@author: rajab
    NASA API to lookup Near Earth Objects, save them as csv files for each dates sorted 
    descending by max diamater"""

# import standard library
import csv
# import third party library
import requests

def main():
    """ run time code"""

    def by_estimated_dia(arg):
        """ return  maximum estimated diamter in meters of the NEO"""
        return arg['estimated_diameter']['meters']['estimated_diameter_max']
    
    with open(r'/home/student/mycode/nasa_api_key') as fh:
        fh = fh.read()
        res = requests.get(f'https://api.nasa.gov/neo/rest/v1/feed?api_key={fh}'.rstrip('\n'))

    if res.status_code == 200:  #check to see the API request is successful
      
        json_obj = res.json()    # return json object of the response
        neo = json_obj.get('near_earth_objects')   #get a list of keys from near_earth_objects dict
        for item in neo:   # loop through the keys
            neolist = json_obj['near_earth_objects'][item]       # assign the list returned from each key to neolist
            wfh = open(f'/home/student/mycode/pythoncert/{item}.csv', 'w', newline='')  # open  filename in write mode
            headers = neolist[0].keys()                        # assign headers
            slist = sorted(neolist, key=by_estimated_dia, reverse=True)  # sort the list by max diameters in descending order
            csv_outfile = csv.DictWriter(wfh, headers, restval='', extrasaction='ignore') # construct csv object
            csv_outfile.writeheader()   # writerow keys of the dict
            csv_outfile.writerows(slist)  #  write values of the list
            wfh.close()   # close the file handle for contents to be written from buffer to the file.
            
    else:
        print(f'Exception {res.status_code} occurred. Retry your request')  # report to user if the status code is anything but 200 
        
                      
if __name__ == "__main__":
    main()
