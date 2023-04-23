import matplotlib.pyplot as plt
import pandas as pd

weekday_data = pd.read_csv(r'C:\Users\14380\Desktop\Python-Projects\比赛开始Data Mining Projects\工作日周末数据\工作日数据.csv')
weekend_data = pd.read_csv(r'C:\Users\14380\Desktop\Python-Projects\比赛开始Data Mining Projects\工作日周末数据\周末数据.csv')
#累加统计
weekday_data_sum = weekday_data['19'].sum()
weekend_data_sum = weekend_data['107'].sum()

print(weekday_data_sum,weekend_data_sum)
plt.bar(x = range(0,2),height=[weekday_data_sum,weekend_data_sum])
plt.grid()
plt.xticks(range(0,2,1),['Week Day','Week End'])
plt.title('The Sum Of Weekdays and Weekends Order Amount')
plt.ylabel('Order Amount')
plt.show()
#平均数
weekday_data_mean = weekday_data['19'].mean()
weekend_data_mean = weekend_data['107'].mean()

print(weekday_data_mean,weekend_data_mean)
plt.bar(x = range(0,2),height=[weekday_data_mean,weekend_data_mean])
plt.xticks(range(0,2,1),['Week Day','Week End'])
plt.title('The Mean Of Weekdays and Weekends Order Amount')
plt.ylabel('Mean')
plt.grid()
plt.show()