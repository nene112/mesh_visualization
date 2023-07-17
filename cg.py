from matplotlib import pyplot as plt
import numpy as np

if __name__ == '__main__':
	np.random.seed(100)
	x = np.linspace(-1, 1, 100).reshape(100, 1)
	y = 3 * np.power(x, 2) + 2 + 0.2 * np.random.rand(x.size).reshape(100, 1)
	plt.scatter(x, y)
	plt.show()

	#初始化随机参数
	w1=np.random.rand(1,1)
	b1=np=np.random.rand(1,1)

	lr=0.001
	for i in range(800):
		y_pred =np.power(x,2)*w1+b1
		loss = 0.5*(y_pred-y)**2
		loss=loss.sum()
		#计算梯度
		grad_w=np.sum((y_pred-y)*np.power(x,2))
		grad_b=np.sum((y_pred-y))
		#使用梯度下降法，使loss最小
		w1-=lr*grad_w
		b1-=lr*grad_b
		plt.plot(x,y_pred,'r-',label='predict')
		plt.scatter(x,y,color='blue',maker='o',label='true')

		plt.xlim(-1,1)
		plt.ylim(2,6)
		plt.legend()
		plt.show()
		print(w1,b1)

