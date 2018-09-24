import csv
import sys

fname = sys.argv[1]
with open(fname) as csvfile:
    reader = csv.reader(csvfile, delimiter=",")
    isHeader = True
    dest = open((fname[0:-4] + "_after.csv"), "w")

    for row in reader:
        if isHeader:
            isHeader = False
            dest.write("Date Time,Open,High,Low,Close,Volume\n")
            continue
        dt = row[0][0:-4]
        dt = (dt[6:10] + "-" + dt[3:5] + "-" + dt[0:2] + " " + dt[11:len(dt)])
        dest.write(dt + "," + row[1] + "," + row[2] + "," + row[3] + "," + row[4] + "," + row[5] + "\n")
