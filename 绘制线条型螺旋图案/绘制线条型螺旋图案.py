# 需求：请使用 Python 的 tkinter 库来创建一个图形界面，并在其中绘制一个由红色线条组成的螺旋形图案
from tkinter import*
# 创建一个 Canvas 组件，用于绘制图形，并设置宽度和高度均为 300 像素，背景色为白色
canvas = Canvas(width=300,height=300,bg="white")
canvas.pack(expand=True,fill=BOTH)

# 初始化第一组线条的起点坐标
x0, y0 = 163,163
# 初始化第一组线条的终点 y 坐标偏移量
y1 = 175
# 绘制第一组螺旋形线条
for i in range(19):
    # 使用 create_line 方法绘制直线，其参数分别代表线条的起点坐标和终点坐标
    # 设置线条宽度为 1 像素，颜色为红色
    canvas.create_line(x0,y0,x0,y1,width=1,fill="red")
    # 更新起点坐标，每次向左上方移动 5 个像素点
    x0, y0 = x0 - 5, y0 - 5
    # 更新终点 y 坐标偏移量，每次增加 5 个像素点
    y1 += 5

# 初始化第二组线条的起点坐标
x0, y0 = 163,163
# 初始化第二组线条的终点 y 坐标偏移量
y1 = 175
# 绘制第二组螺旋形线条
for i in range(19):
    # 使用 create_line 方法绘制直线，其参数分别代表线条的起点坐标和终点坐标
    # 设置线条宽度为 1 像素，颜色为红色
    canvas.create_line(x0, y0, x0, y1, width=1, fill="red")
    # 更新起点坐标，每次向右下方移动 5 个像素点
    x0, y0 = x0 + 5, y0 + 5
    # 更新终点 y 坐标偏移量，每次增加 5 个像素点
    y1 += 5

mainloop()