#!/usr/bin/env python3

import csv
import json
import time
import wayback

wb = wayback.WaybackClient()

for row in csv.DictReader(open('ayo.csv')):
    for url in json.loads(row['entities.urls']):
        results = len(list(wb.search(url['expanded_url'])))
        print(url['expanded_url'], results)
    time.sleep(1)
