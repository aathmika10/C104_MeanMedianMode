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
n=len(newData)
total=0
for x in newData:
    total+=x
mean=total/n
print("mean is "+ str(mean))