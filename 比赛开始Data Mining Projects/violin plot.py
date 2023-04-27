import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv(r'C:\Users\14380\Desktop\Python-Projects\比赛开始Data Mining Projects\异常值处理过后.csv')

print(max(data['19']))

plt.violinplot(data['19'],showmeans=True)
plt.title('Violin Plot Of Order Amount(Data Cleaned)')
plt.grid()
plt.ylabel('Order Amount')
plt.show()