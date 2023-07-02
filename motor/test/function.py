import numpy as np	
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import style
from sklearn.metrics import max_error

# fig, axes = plt.subplots()
class Function():

    def __init__(self,a,b,c):
        self.fig, self.ax = plt.subplots()
        self.x, self.y = [], []
        self.plt = plt
        self.a, self.b, self.c = a, b, c
        self.draw()

    def draw(self):
        a, b, c = self.a, self.b, self.c
        self.x = np.linspace(0,1100,5000)
        for x in self.x:
            self.y.append(-c/(x+a)+0+c/a)      #核心函数
        
        self.ax.set(title="function", xlim=[-10,500], ylim=[-2,60])
        self.ax.plot(self.x, self.y, color='lightcoral', label='F')
        self.ax.legend()
        self.display()

    def display(self):
        self.plt.show()

# Function(a=30, b=2, c=300)
# Function(a=100, b=2, c=1000)

max_force= 25   #c/a
slope = 2000      #c#c


Function(a=slope/max_force, b=2, c=slope)