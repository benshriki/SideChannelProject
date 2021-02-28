import csv

# return number of hits
def getNum(m_str):
    if m_str == ""  or m_str=="None" or m_str[0]=='#':
        return 0
    num = float(m_str)
    return num

#return the key with the most hits in row
def maxInRow(row):
    m_max = 0
    max_key = "Nan"
    for key in row:
        if key == "file" or key == "     addr":
            continue
        tmp = getNum(str(row[key]))
        if m_max < tmp:
            max_key = key
            m_max = tmp
    return max_key, m_max
        
# calculate no noise addresses
def howmanyZero(row):
    counter = 0
    for key in row:
        if key == "file" or key == "     addr":
            continue
        if getNum(str(row[key])) == 0:
            counter += 1
    return counter 
# min delta
def calcminDelta(row,num,k):
    delta = 1000
    for key in row:
        if key == "file" or key == "     addr":
            continue
        tmp = abs(num - getNum(str(row[key])))
        if delta > tmp and k != key:
            delta = tmp
    return delta

fileName = str(input("enter file name:"))
with open(fileName, newline='') as csvfile:
     reader = csv.DictReader(csvfile)
     for row in reader:
        key, num = maxInRow(row)
        delta = calcminDelta(row,num,key)
        if(0.9 <= num and num <= 1.2  ):
           print("file: " + row['file'] + "\taddr:" + row['     addr'] + "\tkey: "+key+"\t%_hits: "+str(num)+"\tdelta: "+str(delta))
