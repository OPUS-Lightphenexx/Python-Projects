import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#各年同季度

#第一季度
#2016年第一季度
Season_1_2016_Data = pd.read_csv(r'C:\Users\14380\Desktop\Python-Projects\比赛开始Data Mining Projects\季度统计\2016年第一季度.csv')
Season_1_2016_ord = Season_1_2016_Data['11'].sum()

#2017年第一季度
Season_1_2017_Data = pd.read_csv(r'C:\Users\14380\Desktop\Python-Projects\比赛开始Data Mining Projects\季度统计\2017年第一季度.csv')
Season_1_2017_ord = Season_1_2017_Data['36'].sum()

#2018年第一季度
Season_1_2018_Data = pd.read_csv(r'C:\Users\14380\Desktop\Python-Projects\比赛开始Data Mining Projects\季度统计\2018年第一季度.csv')
Season_1_2018_ord = Season_1_2018_Data['16'].sum()

#各年第一季度画图开始
height_season_1 = np.array([Season_1_2016_ord,Season_1_2017_ord,Season_1_2018_ord])
plt.bar(x = [1,2,3],height = height_season_1)
labels_season_1 = ['{}'.format(i) for i in ['2016','2017','2018']]
plt.xticks(range(1,4,1),labels_season_1)
plt.xlabel('Years')
plt.ylabel('Order Amount')
plt.title('Season One Sales')
plt.grid()
plt.show()


#第二季度
#2016年第二季度
Season_2_2016_Data = pd.read_csv(r'C:\Users\14380\Desktop\Python-Projects\比赛开始Data Mining Projects\季度统计\2016年第二季度.csv')
Season_2_2016_ord = Season_2_2016_Data['306'].sum()

#2017年第二季度
Season_2_2017_Data = pd.read_csv(r'C:\Users\14380\Desktop\Python-Projects\比赛开始Data Mining Projects\季度统计\2017年第二季度.csv')
Season_2_2017_ord = Season_2_2017_Data['230'].sum()

#2018年第二季度
Season_2_2018_Data = pd.read_csv(r'C:\Users\14380\Desktop\Python-Projects\比赛开始Data Mining Projects\季度统计\2018年第二季度.csv')
Season_2_2018_ord = Season_2_2018_Data['18'].sum()

#各年第二季度画图开始
height_season_2 = np.array([Season_2_2016_ord,Season_2_2017_ord,Season_2_2018_ord])
plt.bar(x = [1,2,3],height=height_season_2,color='red')
labels_season_2 = ['{}'.format(i) for i in ['2016','2017','2018']]
plt.xticks(range(1,4,1),labels_season_2)
plt.xlabel('Years')
plt.ylabel('Order Amount')
plt.title('Season Two Sales')
plt.grid()
plt.show()


#第三季度
#2016年第三季度
Season_3_2016_Data = pd.read_csv(r'C:\Users\14380\Desktop\Python-Projects\比赛开始Data Mining Projects\季度统计\2016年第三季度.csv')
Season_3_2016_ord = Season_3_2016_Data['451'].sum()

#2017年第三季度
Season_3_2017_Data = pd.read_csv(r'C:\Users\14380\Desktop\Python-Projects\比赛开始Data Mining Projects\季度统计\2017年第三季度.csv')
Season_3_2017_ord = Season_3_2017_Data['9'].sum()

#2018年第三季度
Season_3_2018_Data = pd.read_csv(r'C:\Users\14380\Desktop\Python-Projects\比赛开始Data Mining Projects\季度统计\2018年第三季度.csv')
Season_3_2018_ord = Season_3_2018_Data['7'].sum()

#各年第三季度画图开始
height_season_3 = np.array([Season_3_2016_ord,Season_3_2017_ord,Season_3_2018_ord])
plt.bar(x = [1,2,3],height=height_season_3,color='y')
labels_season_3 = ['{}'.format(i) for i in ['2016','2017','2018']]
plt.xticks(range(1,4,1),labels_season_3)
plt.xlabel('Years')
plt.ylabel('Order Amount')
plt.title('Season Three Sales')
plt.grid()
plt.show()



#第四季度
#2016年第四季度
Season_4_2016_Data = pd.read_csv(r'C:\Users\14380\Desktop\Python-Projects\比赛开始Data Mining Projects\季度统计\2016年第四季度.csv')
Season_4_2016_ord = Season_4_2016_Data['46'].sum()

#2017年第四季度
Season_4_2017_Data = pd.read_csv(r'C:\Users\14380\Desktop\Python-Projects\比赛开始Data Mining Projects\季度统计\2017年第四季度.csv')
Season_4_2017_ord = Season_4_2017_Data['51'].sum()

#2018年第四季度
Season_4_2018_Data = pd.read_csv(r'C:\Users\14380\Desktop\Python-Projects\比赛开始Data Mining Projects\季度统计\2018年第四季度.csv')
Season_4_2018_ord = Season_4_2018_Data['4'].sum()

#各年第四季度画图开始
height_season_4 = np.array([Season_4_2016_ord,Season_4_2017_ord,Season_4_2018_ord])
plt.bar(x = [1,2,3],height = height_season_4,color='g')
labels_season_4 = ['{}'.format(i) for i in ['2016','2017','2018']]
plt.xticks(range(1,4,1),labels_season_4)
plt.xlabel('Years')
plt.ylabel('Order Amount')
plt.title('Season Four Sales')
plt.grid()
plt.show()

#2015年第四季度
Season_4_2015_Data = pd.read_csv(r'C:\Users\14380\Desktop\Python-Projects\比赛开始Data Mining Projects\季度统计\2015年第四季度.csv')
Season_4_2015_ord = Season_4_2015_Data['19'].sum()
height_season_4_final  = np.array([Season_4_2015_ord,Season_4_2016_ord,Season_4_2017_ord,Season_4_2018_ord])

#总表
plt.plot([1,2,3],height_season_1,label='Season 1')
plt.plot([1,2,3],height_season_2,color='red',label='Season 2')
plt.plot([1,2,3],height_season_3,color='y',label = 'Season 3')
plt.plot([1,2,3],height_season_4,color='g',label = 'Season 4')
labels_season = ['{}'.format(i) for i in ['2016','2017','2018']]
plt.xticks(range(1,4,1),labels_season)
plt.xlabel('Years')
plt.ylabel('Order Amount')
plt.title('Season Order Amount Plot Graph')
plt.grid()
plt.legend()
plt.show()

#合并起来看看
x_data_all = [Season_1_2016_ord,
          Season_2_2016_ord,
          Season_3_2016_ord,
          Season_4_2016_ord,
          Season_1_2017_ord,
          Season_2_2017_ord,
          Season_3_2017_ord,
          Season_4_2017_ord,
          Season_1_2018_ord,
          Season_2_2018_ord,
          Season_3_2018_ord,
          Season_4_2018_ord]
plt.plot(x_data_all,color='red')
ticks =                          ['2016_1',
                                  '2016_2',
                                  '2016_3',
                                  '2016_4',
                                  '2017_1',
                                  '2017_2',
                                  '2017_3',
                                  '2017_4',
                                  '2018_1',
                                  '2018_2',
                                  '2018_3',
                                  '2018_4']
plt.xticks(range(0,len(x_data_all)),ticks,rotation=45)
plt.bar(x=range(0,len(x_data_all)),height=x_data_all)
plt.xticks(range(0,len(x_data_all)),ticks,rotation=45)
plt.grid()
plt.ylabel('Order Amount')
plt.title('Year-Season Order Amount Descriptive Statistics')
plt.show()