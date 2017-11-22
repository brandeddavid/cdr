import csv
import sys
import os


with open('standard.csv', 'a', newline='') as l, open('test.csv','r') as f:

    fieldnames = ['Caller MSISDN','Callee MSISDN','Date','Time','Duration','Action Type','Caller IMEI','Callee IMEI','Caller IMSI','Callee IMSI','Base Station Position','Base Station ID','EndLocation','Latitude','Longitude','record_type','service_type','Data Source','ROAMING VPMN','CALLER ID/NAME LOOKUP','CALLEE ID/NAME LOOKUP']

    writer = csv.DictWriter(l, fieldnames=fieldnames)

    writer.writeheader()

    reader = csv.reader(f, delimiter=',')

    for row in reader:

        writer.writerow({'Caller MSISDN':row[0],'Callee MSISDN':row[1],'Date':row[2],'Time':row[3],'Duration':row[4],'Action Type':row[5],'Caller IMEI':row[8],'Callee IMEI':None,'Caller IMSI':None,'Callee IMSI':None,'Base Station Position':row[7],'Base Station ID':None,'EndLocation':None,'Latitude':None,'Longitude':None,'record_type':None,'service_type':None,'Data Source':None,'ROAMING VPMN':None,'CALLER ID/NAME LOOKUP':None,'CALLEE ID/NAME LOOKUP':None})

FIRST_ROW_NUM = 0
ROWS_TO_DELETE = {1}

with open('standard.csv', 'rt') as infile, open('toIngest.csv', 'wt') as outfile:
    outfile.writelines(row for row_num, row in enumerate(infile, FIRST_ROW_NUM)
                        if row_num not in ROWS_TO_DELETE)

os.remove('standard.csv')
