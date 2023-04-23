import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn import linear_model
from sklearn.tree import DecisionTreeRegressor

read_csv1 = pd.read_csv(r"C:\Users\14380\Desktop\Python-Projects\比赛开始Data Mining Projects\目标数据\order_train1.csv")
#先综述统计
x = read_csv1['ord_qty']
plt.plot(x)
plt.scatter(range(0,len(x)),x,color='red')
plt.xlabel('Item Code')
plt.ylabel('Item Price')
plt.title('Item Code-Price')
plt.grid()
plt.show()

#决策树回归模型
read_csv2 = pd.read_csv(r'C:\Users\14380\Desktop\Python-Projects\比赛开始Data Mining Projects\order_train2 final.csv')

print(read_csv2)
x_data = read_csv2[['year','month','day','first_cate_code','second_cate_code']]

print(x_data)
#x_data = read_csv2[:,0:2]
#print(x_data)


y_ord = read_csv2

model1 = linear_model.LinearRegression()
model2 = DecisionTreeRegressor()

