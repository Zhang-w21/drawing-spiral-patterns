from tkinter import*
canvas = Canvas(width=400,height=400,bg="white")
canvas.pack(expand=True,fill=BOTH)
# 绘制 19 个矩形，形成螺旋形图案

# 初始化第一个矩形的左上角坐标
x0, y0 = 163, 163
# 初始化第一个矩形的右下角坐标
x1, y1 = 175, 175
x0, y0 = 163, 163
for i in range(19):
    canvas.create_rectangle(x0,y0,x1,y1)
    # 更新坐标
    x0 -= 5
    y0 -= 5
    x1 += 5
    y1 += 5
mainloop()