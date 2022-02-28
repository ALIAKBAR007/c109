import csv 
import plotly.figure_factory as pf
import pandas as pd
import statistics as st

file = pd.read_csv("c108.csv")

hl=file["Height(Inches)"].to_list()
Wl=file["Weight(Pounds)"].to_list()

#fig=pf.create_distplot([Wl],["xyz"],show_hist=False)

mean = st.mean(hl)
median = st.median(hl)
mode = st.mode(hl)

print("Mean of hl is {}" .format(mean))
print("Median of hl is {}" .format(median))
print("Mode of hl is {}" .format(mode))

ST=st.stdev(hl)
print("ST is {}" .format (ST))

min1= mean-ST
max1= mean+ST
firstSDList=[]
for o in hl:
    if o>min1 and o<max1:
        firstSDList.append(o)

a=len(firstSDList)
total=len(hl)

P=(a*100)/total

print("{}% of hl" .format(P))
