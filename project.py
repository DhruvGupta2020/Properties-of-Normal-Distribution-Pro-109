import pandas as pd
import statistics   

df = pd.read_csv("data.csv")
data = df["Weight(Pounds)"].tolist()

mean = statistics.mean(data)

std = statistics.stdev(data)

range1_start,range1_end = mean-std,mean+std


range2_start,range2_end = mean-std*2,mean+std


range3_start,range3_end = mean-std*3,mean+std*3


range1 = []
for i in data:
    if i>range1_start and i<range1_end:
        range1.append(i)

range2 = []
for d in data:
    if d>range2_start and d<range2_end:
        range2.append(d)

range3 = []
for a in data:
    if a>range3_start and a<range3_end:
        range3.append(a)


p1 = len(range1)*100/len(data)
print(p1)

p2 = len(range2)*100/len(data)
print(p2)

p3 = len(range3)*100/len(data)
print(p3)









    

