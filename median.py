import csv
import plotly_express as px
with open('HeightWeight.csv', newline='') as f:
    read=csv.reader(f)
    file_data=list(read)

file_data.pop(0)
newdata=[]
for i in range(len(file_data)):
    num=file_data[i][1]
    newdata.append(float(num))

n=len(newdata)
newdata.sort()

if (n%2==0):
    median1=float(newdata[n//2])
    median2=float(newdata[n//2-1])
    median=(median1+median2)/2

else:
    median=newdata[n//2]

print(str(median))    

