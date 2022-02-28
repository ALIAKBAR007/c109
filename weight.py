import csv 
import plotly.figure_factory as pf
import pandas as pd
import statistics as st

file = pd.read_csv("c108.csv")

hl=file["Height(Inches)"].to_list()
Wl=file["Weight(Pounds)"].to_list()

#fig=pf.create_distplot([Wl],["xyz"],show_hist=False)

mean = st.mean(Wl)
median = st.median(Wl)
mode = st.mode(Wl)

print("Mean of Wl is {}" .format(mean))
print("Median of Wl is {}" .format(median))
print("Mode of Wl is {}" .format(mode))

ST=st.stdev(Wl)
print("ST is {}" .format (ST))

min1= mean-3*ST
max1= mean+3*ST
firstSDList=[]
for o in Wl:
    if o>min1 and o<max1:
        firstSDList.append(o)

a=len(firstSDList)
total=len(Wl)

P=(a*100)/total

print("{}% 3rd of Wl" .format(P))
