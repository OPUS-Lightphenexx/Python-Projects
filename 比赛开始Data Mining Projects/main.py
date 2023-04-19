import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from matplotlib.font_manager import FontProperties  # 导入FontProperties
my_font = FontProperties(fname="C:\Windows\Fonts\simkai.ttf", size=14)  # 设置字体

#原始训练数据
read_csv1 = pd.read_csv(r"C:\Users\14380\Desktop\Python-Projects\比赛开始Data Mining Projects\目标数据\order_train1.csv")
print(read_csv1)

#数据质量观察
Check_unique = read_csv1.index.nunique()
Check_info = read_csv1.info()
Check_Describe = read_csv1.describe()
print(Check_unique)
print(Check_info)
print(Check_Describe)

#透视表(根据时间和产品类别来划分)
pivot_table_predict4 = read_csv1.pivot_table(index=['order_date','first_cate_code','second_cate_code'],values=['ord_qty'],aggfunc=sum)
print(pivot_table_predict4)
pivot_table_predict4.to_excel('时间-销售总量透视表.xlsx')

#处理离散值
#画出boxplot(没清洗前)
plt.boxplot(read_csv1['ord_qty'])
plt.title('Ord Qty Boxplot(Not yet Cleaned)')
plt.show()
plt.boxplot(read_csv1['item_price'])
plt.title('Item Price Boxplot(Not Yet Cleaned)')
plt.show()
plt.boxplot([read_csv1['ord_qty'],read_csv1['item_price']],showfliers=False)
plt.show()
#离群值处理了的
plt.boxplot(read_csv1['ord_qty'],showfliers=False,showmeans=True)
plt.title('Ord Qty Boxplot')
plt.show()
plt.boxplot(read_csv1['item_price'],showfliers=False)
plt.title('Item Price Boxplot')
plt.show()

#画图类
#第一问画图
#没有数据清洗前
x = read_csv1['item_price']
y = read_csv1['ord_qty']
plt.scatter(x,y)
plt.xlabel('Price')
plt.ylabel('Order amount')
plt.title('Price-Needs')
cov = np.cov(x,y)
plt.grid()
print(cov)
plt.show()

#根据销售区域代码随着代码的增加
pivot_table_region = read_csv1.pivot_table(index=['sales_region_code'],values=['ord_qty'],aggfunc=sum)
print(pivot_table_region)
plt.bar(x=pivot_table_region.index,height=pivot_table_region['ord_qty'])
plt.xlabel('Regions')
plt.ylabel('Order amount')
plt.title('Region-Needs')
plt.grid()
plt.show()

#violin图(数据清洗过后，先清洗一遍)(回来再看)
Q3 = 101
Q1 = 10

IQR = Q3 - Q1
upper = read_csv1['ord_qty'] >= (Q3+1.5*IQR)
lower = read_csv1['ord_qty'] <= (Q1-1.5*IQR)
print(lower)
print(upper)
upper_listing = list(upper)
print(upper_listing)


#线下线上售卖情况
pivot_table_sales_chan = read_csv1.pivot_table(index=['sales_chan_name'],values=['ord_qty'],aggfunc=sum)
#print(pivot_table_sales_chan)
plt.bar(x=pivot_table_sales_chan.index,height=pivot_table_sales_chan['ord_qty'])
plt.xlabel('Order Type')
plt.ylabel('Order Amount')
plt.title('Order Type-Needs')
plt.grid()
plt.show()

#细类画图
#第一类
pivot_table_sales_first_cate = read_csv1.pivot_table(index=['first_cate_code'],values=['ord_qty'],aggfunc=sum)
#print(pivot_table_sales_first_cate)
plt.bar(x=pivot_table_sales_first_cate.index,height=pivot_table_sales_first_cate['ord_qty'])
plt.title('First Class-Needs')
plt.xlabel('First Class')
plt.ylabel('Order Amount')
x = range(301,309,1)
plt.xticks(x)
plt.grid()
plt.show()
#第二类
pivot_table_sales_second_cate = read_csv1.pivot_table(index=['second_cate_code'],values=['ord_qty'],aggfunc=sum)
#print(pivot_table_sales_second_cate)
plt.bar(x=pivot_table_sales_second_cate.index,height=pivot_table_sales_second_cate['ord_qty'])
plt.title('Second Class-Needs')
plt.xlabel('Second Class')
plt.ylabel('Order Amount')
x = range(401,413,1)
plt.xticks(x)
plt.grid()
plt.show()




