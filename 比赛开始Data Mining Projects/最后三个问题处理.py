import pandas as pd
import matplotlib.pyplot as plt

read_csv = pd.read_csv(r'C:\Users\14380\Desktop\Python-Projects\比赛开始Data Mining Projects\order_train2.csv')
print(read_csv)

#节假日对产品需求量的影响
Time_Month_0 = read_csv[read_csv['Time_of_Month']==0]
print(Time_Month_0)
Time_Month_0_ord = Time_Month_0['ord_qty'].sum()

Time_Month_1 = read_csv[read_csv['Time_of_Month']==1]
print(Time_Month_1)
Time_Month_1_ord = Time_Month_1['ord_qty'].sum()

Time_Month_2 = read_csv[read_csv['Time_of_Month']==2]
print(Time_Month_2)
Time_Month_2_ord = Time_Month_2['ord_qty'].sum()

Time_Month_X_Data = [Time_Month_0_ord,
                     Time_Month_1_ord,
                     Time_Month_2_ord]
plt.plot(Time_Month_X_Data,color='red')
plt.bar(x=range(0,len(Time_Month_X_Data)),height=Time_Month_X_Data)
plt.xticks(range(0,3),['Start Month','Middle Month','End Month'])
plt.ylabel('Order Amount')
plt.title('The Characteristics of Product Demand in Different Time Periods')
plt.grid()
plt.show()

#节假日对产品需求量的影响
holiday = read_csv[read_csv['Holiday']==1].mean()
non_holiday = read_csv[read_csv['Holiday']==0].mean()

plt.bar(x=range(0,2),height=[holiday,non_holiday])
plt.show()

#促销（如618、双十一等）对产品需求量的影响

