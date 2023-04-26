from sklearn.impute import KNNImputer
import pandas as pd
import numpy as np

nan_data = pd.read_csv(r'C:\Users\14380\Desktop\Python-Projects\比赛开始Data Mining Projects\需求最终表(标出了在原始数据里面没有的数据).csv')
print(nan_data)

imputer = KNNImputer(n_neighbors=2)
fill = imputer.fit_transform(np.array(nan_data['ord_qty']).reshape(-1,1))
print(fill)
print(len(fill))