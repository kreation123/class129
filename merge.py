import csv
dataset1  = []
dataset2 = []
with open('data2.csv','r') as f:
    csvreader  = csv.reader(f)
    for row in csvreader:
        dataset1.append(row)
with open('newdataset2.csv' , 'r') as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        dataset2.append(row)
header1 = dataset1[0]
planetdata1 = dataset1[1:]
header2 = dataset2[0]
planetdata2 = dataset2[1:]
headers = header1 + header2
planetdatas = []
for index,datarow in enumerate(planetdata1):
    planetdatas.append(planetdata1[index]+planetdata2[index])
with open('merge.csv','a+') as f:
    csvwriter  = csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(planetdatas)


