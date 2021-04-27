import matplotlib.pyplot as plt
from matplotlib.figure import figaspect
from tqdm import tqdm  #用于显示进度
import numpy as np

ratio = 9/16 #设置图片比例 the ratio  = height / width).

w, h = figaspect(ratio)# return width,height 和ratio相反，非常神奇的脑回路
plt.rcParams['figure.figsize'] = (w, h) #按比例设置图片大小

fig = plt.figure(constrained_layout=True)
fig.set_constrained_layout_pads(hspace = 0)
gs = fig.add_gridspec(1, 1)#设置fig上要画多少行多少列的图片（即多张图画在一个fig上，如果只画一张图就（1，1）即可）

for i in tqdm(range(3)):#生成1000张图
	t = np.arange(0.0, 2.0, 0.01)
	s = i*np.sin(2 * i*np.pi * t)
	ax1 = fig .add_subplot(gs[0, :]) #将fig的第一行全给坐标轴1 ax1
	ax1.plot(t,s, linewidth=0.75,label = 'legend')
	ax1.set_title('station', fontdict={'family' : 'Times New Roman', 'size'   : 16})
	'''设置网格 包括网格间隔、线度、样式'''
	ax1.xaxis.set_major_locator(plt.MultipleLocator(0.5))
	ax1.xaxis.set_minor_locator(plt.MultipleLocator(0.1))
	ax1.yaxis.set_major_locator(plt.MultipleLocator(0.5))
	ax1.yaxis.set_minor_locator(plt.MultipleLocator(0.1))
	ax1.grid(which='major', axis='x', linewidth=0.75, linestyle='-', color='0.75')
	ax1.grid(which='minor', axis='x', linewidth=0.25, linestyle='-', color='0.75')
	ax1.grid(which='major', axis='y', linewidth=0.75, linestyle='-', color='0.75')
	ax1.grid(which='minor', axis='y', linewidth=0.25, linestyle='-', color='0.75')
	ax1.grid(True, which='both')
	'''设置坐标标题'''
	ax1.set_ylabel('y', fontdict={'family' : 'Times New Roman', 'size'   : 16})
	ax1.set_xlabel('t', fontdict={'family' : 'Times New Roman', 'size'   : 16})
	'''设置图例'''
	ax1.legend(loc="lower left",prop={'family' : 'Times New Roman', 'size'   : 16})  

	'''设置刻度字体大小，刻度默认用major的值显示'''
	ax1.tick_params(labelsize=15) 
	#x\y轴坐标分别用了两种设置方式 方便学习
	ax1.xaxis.set_major_formatter(lambda x, pos: str(x)+'s')  # 把major刻度的值转化掉为str 加上's'

	a =  np.linspace(0,1,6)# 把刻度变为每隔0.2一次，或者np.arange(0,1,0.2) 
	b = ['%.2f'%oi for oi in a] # #Y轴的刻度标签，为字符串形式，.2f表示小数点两位
	plt.yticks(a,b)  
	plt.yticks(fontproperties = 'Times New Roman', size = 14)
	plt.xticks(fontproperties = 'Times New Roman', size = 14)
	plt.savefig("/Users/Liang/Desktop/"+str(i)+".jpg", dpi = 200) #按i.jpg保存图片
	plt.clf()