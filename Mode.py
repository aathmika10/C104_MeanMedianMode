from collections import Counter
import csv
with open('HeightWeight.csv',newline='')as f:
    reader=csv.reader(f)
    data=list(reader)

data.pop(0)

newData=[]
for i in range(len(data)):
    # 1 is height
    number=data[i][1]
    newData.append(float(number))

count=Counter(newData)
ModeDataForRange={
    "50-60":0,
    "60-70":0,
    "70-80":0
}

for height, occurence in count.items():
    if 50<float(height)<60:
        ModeDataForRange["50-60"]+=occurence
    elif 60<float(height)<70:
        ModeDataForRange["60-70"]+=occurence
    elif 70<float(height)<80:
        ModeDataForRange["70-80"]+=occurence

    modeRange,modeOccurence= 0,0
    for range,occurence in ModeDataForRange.items():
        if occurence>modeOccurence:
            modeRange,modeOccurence=[int(range.split("-")[0]),int(range.split("-")[1])],occurence
mode=float((modeRange[0]+modeRange[1])/2)
print(f"Mode is -> {mode:2f}")