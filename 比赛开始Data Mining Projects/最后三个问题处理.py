import pandas as pd
import matplotlib.pyplot as plt

read_csv = pd.read_csv(r'C:\Users\14380\Desktop\Python-Projects\比赛开始Data Mining Projects\order_train2.csv')

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
holiday = read_csv[read_csv['Holiday']==1]
holiday_ord_mean = holiday['ord_qty'].mean()
non_holiday = read_csv[read_csv['Holiday']==0]
non_holiday_ord_mean = non_holiday['ord_qty'].mean()

plt.bar(x=range(0,2),height=[holiday_ord_mean,non_holiday_ord_mean])
plt.xticks(range(0,2),['Holiday','Non Holiday'])
plt.title('The Mean Of Order Amount on Holidays and Non Holidays')
plt.ylabel('Order Amount')
plt.grid()
plt.show()

#促销（如618、双十一等）对产品需求量的影响
read_csv1 = pd.read_csv(r'C:\Users\14380\Desktop\Python-Projects\比赛开始Data Mining Projects\order_train3.csv')
discount = read_csv1[read_csv1['Discount']==1]
discount_ord_mean = discount['ord_qty'].mean()
non_discount = read_csv1[read_csv1['Discount']==0]
non_discount_ord_mean = non_discount['ord_qty'].mean()

plt.bar(x=range(0,2),height=[discount_ord_mean,non_discount_ord_mean])
plt.xticks(range(0,2),['Discount','Non Discount'])
plt.ylabel('Order Amount')
plt.grid()
plt.show()


