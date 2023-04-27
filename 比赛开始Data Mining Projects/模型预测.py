import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn import linear_model
from sklearn.tree import DecisionTreeRegressor
from 缺失值处理 import fill

#先进行异常值ko
data = pd.read_csv(r"C:\Users\14380\Desktop\Python-Projects\比赛开始Data Mining Projects\目标数据\order_train1.csv")
Q3 = 101
Q1 = 10

IQR = Q3 - Q1
int_ord_qty = data['ord_qty'].astype(int)

upper = (Q3+1.5*IQR)
lower = (Q1-1.5*IQR)
print('l',lower)
print('u',upper)


#Correct = (Q3+1.5*IQR) <= data['ord_qty'] <= (Q1-1.5*IQR)


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
read_csv2 = pd.read_csv(r'C:\Users\14380\Desktop\Python-Projects\比赛开始Data Mining Projects\异常值处理过后.csv')
read_csv2.columns= data.columns

print(read_csv2)
x_data = read_csv2[['sales_region_code','first_cate_code','second_cate_code','item_code']]
y_data = read_csv2['ord_qty']
print(x_data)
#x_data = read_csv2[:,0:2]
#print(x_data)


y_ord = read_csv2

model1 = linear_model.LinearRegression()
model2 = DecisionTreeRegressor(max_depth=23,random_state=True)
from sklearn.ensemble import RandomForestRegressor
model3 = RandomForestRegressor()


predict_read = pd.read_csv(r'C:\Users\14380\Desktop\Python-Projects\比赛开始Data Mining Projects\需求最终表(标出了在原始数据里面没有的数据).csv')
x_predict_data = predict_read[['sales_region_code','first_cate_code','second_cate_code','item_code']]


model2.fit(x_data,y_data)
predict2 = model2.predict(x_predict_data)
print(model2.score(x_data,y_data))
print(predict2)

model1.fit(x_data,y_data)
predict1 = model1.predict(x_predict_data)
print(model1.score(x_data,y_data))
print(predict1)

#model3.fit(x_data,y_data)
#predict3 = model3.predict(x_predict_data)
#print(model3.score(x_data,y_data))
#print(predict3)


plt.scatter(range(0,len(predict2)),predict2,color='green')
plt.plot(range(0,len(predict2)),predict2,color='red')
plt.grid()
plt.xlabel('Predict')
plt.ylabel('Order Amount')
plt.title('Prediction Using Decision Tree Regressor')
plt.show()
plt.scatter(range(0,len(predict1)),predict1)
plt.xlabel('Predict')
plt.ylabel('Order Amount')
plt.title('Prediction Using Linear Regression')
plt.grid()
plt.show()

#数据存储

print(len(predict_read['sales_region_code']))
print(len(predict2))
predict_read['线性回归预测'] = np.round(predict1)
predict_read['决策树回归预测'] = np.round(predict2)

predict_read.to_excel('Final test.xlsx')
print(predict_read)
