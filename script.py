import csv
import sys
import os


for arg in sys.argv:

    if sys.argv.index(arg) > 0:

        with open('standard.csv', 'a', newline='') as l, open(arg,'r') as f:

            fieldnames = ['Caller MSISDN','Callee MSISDN','Date','Time','Duration','Action Type','Caller IMEI','Callee IMEI','Caller IMSI','Callee IMSI','Base Station Position','Base Station ID','EndLocation','Latitude','Longitude','record_type','service_type','Data Source','ROAMING VPMN','CALLER ID/NAME LOOKUP','CALLEE ID/NAME LOOKUP']

            writer = csv.DictWriter(l, fieldnames=fieldnames)

            writer.writeheader()

            reader = csv.reader(f, delimiter=',')

            for row in reader:

                writer.writerow({'Caller MSISDN':row[0],'Callee MSISDN':row[1],'Date':row[5],'Time':row[5],'Duration':row[6],'Action Type':row[4],'Caller IMEI':row[9],'Callee IMEI':None,'Caller IMSI':row[11],'Callee IMSI':None,'Base Station Position':row[8],'Base Station ID':row[7],'EndLocation':None,'Latitude':None,'Longitude':None,'record_type':row[2],'service_type':row[3],'Data Source':None,'ROAMING VPMN':row[12],'CALLER ID/NAME LOOKUP':row[13],'CALLEE ID/NAME LOOKUP':None})

FIRST_ROW_NUM = 0
ROWS_TO_DELETE = {1}

with open('standard.csv', 'rt') as infile, open('/home/ibrahim/Downloads/newcdr/datasets/awaiting/' + os.path.basename(arg), 'wt') as outfile:
    outfile.writelines(row for row_num, row in enumerate(infile, FIRST_ROW_NUM)
                        if row_num not in ROWS_TO_DELETE)

os.remove('standard.csv')
