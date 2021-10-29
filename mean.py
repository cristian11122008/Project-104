import csv
with open('HeightWeight.csv', newline='') as f:
    read=csv.reader(f)
    file_data=list(read)

file_data.pop(0)
newdata=[]
for i in range(len(file_data)):
    num=file_data[i][1]
    newdata.append(float(num))

n=len(newdata)
total=0
for x in newdata:
    total=total+x

mean=total/n
print(str(mean))



