import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random

df=pd.read_csv("school1.csv")
data=df['Math_score'].tolist()

def random_set_of_means(counter):
    data_set=[]
    for i in range(0,counter):
        random_index=random.randint(0,len(data)-1)
        value=data[random_index]
        data_set.append(value)
    mean=statistics.mean(data_set)
    return mean

mean_list=[]
for i in range(0,1000):
    set_of_mean=random_set_of_means(100)
    mean_list.append(set_of_mean)

mean=statistics.mean(mean_list)
std_dev=statistics.stdev(mean_list)
print("Mean of sample: ",mean)
print("Standard deviation of sample: ",std_dev)



first_stdev_start,first_stdev_end=mean-std_dev,mean+std_dev
second_stdev_start,second_stdev_end=mean-(2*std_dev),mean+(2*std_dev)
third_stdev_start,third_stdev_end=mean-(3*std_dev),mean+(3*std_dev)

df1=pd.read_csv("School_1_Sample.csv")
data1=df1["Math_score"].tolist()
mean_of_sample1=statistics.mean(data1)

fig=ff.create_distplot([mean_list],['Mathscore'],show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.2],mode="lines",name="mean"))
fig.add_trace(go.Scatter(x=[mean_of_sample1,mean_of_sample1],y=[0,0.2],mode="lines",name="mean_of_sample1"))

fig.add_trace(go.Scatter(x=[first_stdev_start,first_stdev_start],y=[0,0.2],mode="lines",name="1_stdev_start"))
fig.add_trace(go.Scatter(x=[first_stdev_end,first_stdev_end],y=[0,0.2],mode="lines",name="1_stdev_end"))

fig.add_trace(go.Scatter(x=[second_stdev_start,second_stdev_start],y=[0,0.2],mode="lines",name="2_stdev_start"))
fig.add_trace(go.Scatter(x=[second_stdev_end,second_stdev_end],y=[0,0.2],mode="lines",name="2_stdev_end"))

fig.add_trace(go.Scatter(x=[third_stdev_start,third_stdev_start],y=[0,0.2],mode="lines",name="3_stdev_start"))
fig.add_trace(go.Scatter(x=[third_stdev_end,third_stdev_end],y=[0,0.2],mode="lines",name="3_stdev_end"))

fig.show()

z_score=(mean_of_sample1-mean)/std_dev
print('The z_score of sample 1 is: ',z_score)