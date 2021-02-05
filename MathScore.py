import csv
import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics

df = pd.read_csv("data.csv")

mathScore= df["math score"].tolist()

mean=statistics.mean(mathScore)
sd=statistics.stdev(mathScore)
median=statistics.median(mathScore)
mode=statistics.mode(mathScore)

print("Mean =",mean)
print("Median =",median)
print("Mode =",mode)
print("Standard Deviation =",sd)

sd1Start, sd1End= mean-sd, mean+sd
sd2Start, sd2End= mean-(2*sd), mean+(2*sd)
sd3Start, sd3End= mean-(3*sd), mean+(3*sd)

listOfDataWithin1sd = [result for result in mathScore if result>sd1Start and result<sd1End]
listOfDataWithin2sd = [result for result in mathScore if result>sd2Start and result<sd2End]
listOfDataWithin3sd = [result for result in mathScore if result>sd3Start and result<sd3End]

print("{}% of data lies in 1SD".format(len(listOfDataWithin1sd)*100.0/len(mathScore)))
print("{}% of data lies in 2SD".format(len(listOfDataWithin2sd)*100.0/len(mathScore)))
print("{}% of data lies in 3SD".format(len(listOfDataWithin3sd)*100.0/len(mathScore)))

fig = ff.create_distplot([mathScore],["Result"],show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean], y=[0,0.17],mode="lines", name="mean"))
fig.add_trace(go.Scatter(x=[sd1Start,sd1Start], y=[0,0.17],mode="lines", name="Sd1"))
fig.add_trace(go.Scatter(x=[sd1End,sd1End], y=[0,0.17],mode="lines", name="SD1"))
fig.add_trace(go.Scatter(x=[sd2Start,sd2Start], y=[0,0.17],mode="lines", name="SD2"))
fig.add_trace(go.Scatter(x=[sd2End,sd2End], y=[0,0.17],mode="lines", name="SD2"))
fig.add_trace(go.Scatter(x=[sd3Start,sd3Start], y=[0,0.17],mode="lines", name="SD3"))
fig.add_trace(go.Scatter(x=[sd3End,sd3End], y=[0,0.17],mode="lines", name="SD3"))

fig = ff.create_distplot([df["math score"].tolist()],["Math Score"],show_hist=False)
fig.show()