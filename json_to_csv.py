#!/usr/bin/env python
# coding: utf-8

# In[10]:

#It is not showing
from operator import itemgetter        
import csv
import json

output_csv = "C:\\Users\\abhin\\Downloads\\Earlier\\tweet_details.csv"
input_json = "C:\\Users\\abhin\\Downloads\\Earlier\\twitter_tweets1.json"

header = ['created_at']

dict1={}
dict2={}
columns = itemgetter(*header)

json.dumps([dict1, dict2])
with open(input_json) as f_input:
    data = f_input.read()
    tweet_data = json.loads(data)
    with open(output_csv, 'w', newline = '\n') as f_output:
        csv_output = csv.writer(f_output)
        csv_output.writerow(header)
        #for line in tweet_data:
        #    csv_output.writerow([line.get(header)])
        for row in tweet_data:
            if row.strip():
                csv_output.writerow(columns(json.loads(row)))

