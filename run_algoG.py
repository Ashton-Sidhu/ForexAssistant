# -*- coding: utf-8 -*-

import requests
import time
from bs4 import BeautifulSoup
import csv
import os
import dropbox

def loadapi(apikey):
    contents = requests.get(apikey)
    soup = BeautifulSoup(contents.text, 'html.parser')
    price = float(soup.find(id="yfs_l10_usdcad=x").next_element)
    return price

def writeToFile(filename, pricelist):
    os.remove(filename)
    with open(filename, 'w') as file:
        writer = csv.writer(file)
        writer.writerow(pricelist)

def main():
    counter = 1
    prices = []

    while True:
        print(counter)
        try:
            prices.append(loadapi('https://ca.finance.yahoo.com/q?s=USDCAD=X'))
            if(len(prices) < 600):
                writeToFile('data.csv', prices)
            else:
                del prices[0]
                writeToFile('data.csv', prices)

            counter += 1
            time.sleep(30)
        except KeyboardInterrupt:
            #writeToFile(prices)
            print("User Stopped")
            break

if __name__ == "__main__":
    main()
