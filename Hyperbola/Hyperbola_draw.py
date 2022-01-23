
class hyperbola():

    def __init__(self,ax_range=100,line_range=200):
        import matplotlib.pyplot as plt
        # self.a = a
        # self.b = b
        self.x = []
        self.y = []
        self.fig, self.ax = plt.subplots()
        self.plt = plt
        self.ax_range = ax_range
        self.line_range = line_range
        # self.focus = focus


    def hb_data(self,a,b,focus='x'):

        import math
        import numpy as np
        self.a, self.b, self.focus = a, b, focus
        line_range =  self.line_range
        c = math.sqrt(a**2 + b**2)
        foucs_1 = [-c,0]
        foucs_2 = [c,0]
        x1 = list(np.linspace(-line_range,-a,line_range*10))

        y = []
        for x_ in x1:
            dot = math.sqrt(abs((b*x_/a)**2-b**2))
            y.append(dot)
            y.append(-dot)

        x1 =  x1 + x1[::-1]
        y.sort(reverse=True)
        x2 = list(np.linspace(a,line_range,line_range*10))
        x2 = x2[::-1] + x2

        self.data = x1,y,x2


    def hb_draw(self,line_color='lightcoral'):
        ax,data = self.ax, self.data
        if self.focus == 'x':
            ax.plot(data[0], data[1], color=line_color, label='hyperbola')
            ax.plot(data[2], data[1], color=line_color)
        elif self.focus == 'y':
            ax.plot(data[1], data[0], color=line_color, label='hyperbola')
            ax.plot(data[1], data[2], color=line_color)
        else:
            print('You maked an error on focus!!!')

        self.decorate()


    def decorate(self):
        ax, ax_range = self.ax, self.ax_range
        ax.spines['top'].set_visible(False)     #顶边界不可见
        ax.xaxis.set_ticks_position('bottom')  # ticks 的位置为下方，分上下的。
        ax.spines['right'].set_visible(False)   #右边界不可见
        ax.yaxis.set_ticks_position('left')

        # 移动边界，按 Axes 的百分比位置
        ax.spines['bottom'].set_position(('axes', 0.5))
        ax.spines['left'].set_position(('axes', 0.5))

        ax.set(title='Draw Hyperbola', xlim=[-ax_range,ax_range], ylim=[-ax_range,ax_range])
        ax.legend()


    def asymptote(self,ax_color='skyblue'):
        import numpy as np

        line_range = self.line_range
        x = list(np.linspace(-line_range,line_range,10))        #渐近线
        y = [(self.b/self.a)*x_ for x_ in x]
        if self.focus == 'x':
            self.ax.plot(x, y, color=ax_color)
            self.ax.plot(x[::-1], y, color=ax_color)
        elif self.focus == 'y':
            self.ax.plot(y, x, color=ax_color)
            self.ax.plot(y, x[::-1], color=ax_color)

    def display(self):
        self.plt.show()


if __name__ == '__main__':
    h = hyperbola(30,100)
    h.hb_data(10,13,focus='x')
    h.hb_draw()
    h.asymptote()
    h.hb_data(10,13,focus='y')
    h.hb_draw('black')
    h.asymptote('red')

    h.display()

