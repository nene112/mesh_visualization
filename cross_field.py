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
# ax.quiverkey(q, X=0.8, Y=1.5, U=10,
#              label='Quiver key, length = 10', labelpos='E')

# 绘制十字交叉场,坐标点处交叉·
q = ax.quiver(X, Y, U, V, units='xy', scale=2,
              headwidth=0, headlength=0, headaxislength=0)

print(X)
U_v = np.copy(X)
V_v = np.copy(Y)
U_v[::] = U[::]/np.sqrt(U[::]*U[::]+V[::]*V[::])
V_v[::] = V[::]/np.sqrt(U[::]*U[::]+V[::]*V[::])

U_n = np.copy(U)
V_n = np.copy(V)
U_n[::] = -V[::]/np.sqrt(U[::]*U[::]+V[::]*V[::])
V_n[::] = U[::]/np.sqrt(U[::]*U[::]+V[::]*V[::])

X_n = np.copy(X)
Y_n = np.copy(Y)
# 如果要绘制比较好看的十字交叉场，需要下列系数,如果计算域量级发生变化，需要相应修改
X_n[::] = X[::] + 0.2*(U_v[::]-U_n[::])
Y_n[::] = Y[::] + 0.3*(V_v[::]-V_n[::])
q = ax.quiver(X_n, Y_n, -V, U, units='xy', scale=2,
              headwidth=0, headlength=0, headaxislength=0)
print("x[::] ")
print(X)

plt.show()
# 保存图片
plt.savefig('cross_plot.png')  # 指定保存的文件名和格式
