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

newData.sort()
if n%2==0 :
    median1=float(newData[n//2])
    median2=float(newData[n//2-1])
    median=(median1+median2)/2

else:
    median=newData[n//2+1]
    print(n)

print("Median is "+ str(median))
print(f"median is {median}")