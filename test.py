import numpy as np

import matplotlib.pyplot as plt

# 生成随机数据
x = np.random.rand(50)
y = np.random.rand(50)

# 绘制散点图
plt.scatter(x, y, color='blue', marker='o')

plt.title('Scatter Plot Example')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')

plt.show()