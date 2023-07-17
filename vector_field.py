import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

dirpath = './sve_cloud/python_visualization/'
file_path = '20230717_outputcross.dat'  # .dat文件的路径
# 使用NumPy的loadtxt()函数读取文件内容
data = pd.read_csv(file_path, delimiter='\s+', header=None)

# print(data)
x = data[0].values
y = data[1].values
print(x)
print(y)

X = x
Y = y
# X = np.arange(-10, 10, 1)
# Y = np.arange(-10, 10, 1)
print(X)
# U, V = np.meshgrid(X, Y)
U = data[2].values
V = data[3].values
fig, ax = plt.subplots(figsize=(11, 7), dpi=300)
q = ax.quiver(X, Y, U, V, linewidth=0.5)
q = ax.quiver(X, Y, -V, U, linewidth=0.5)
ax.quiverkey(q, X=0.8, Y=1.5, U=10,
             label='Quiver key, length = 10', labelpos='E')

# # 绘制十字交叉场
# q = ax.quiver(X, Y, U, V, units='xy', scale=1,
#               headwidth=0, headlength=0, headaxislength=0)
# q = ax.quiver(X+0.5, Y-0.5, -V, U, units='xy', scale=1,
#               headwidth=0, headlength=0, headaxislength=0)


# 添加十字交叉图例
ax.plot(0, 0, 'k+', markersize=10)


plt.show()
# 保存图片
plt.savefig('plot.png')  # 指定保存的文件名和格式
