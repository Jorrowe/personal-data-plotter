import numpy as np
import matplotlib.pyplot as plt


class DataPlotter:
    def __init__(self, xData, yData):
        self.xData = xData
        self.yData = yData
        self.fig, self.ax = plt.subplots()
    

    def plotData(self, pointSize=15, color=[0,0,0], name="Data"):
        self.ax.scatter(self.xData, self.yData, s=pointSize, c=[color], label=name)


    def plotErrors(self, xError= 0, yError = 0, color = [0.5, 0.5, 0.5]):
        self.ax.errorbar(self.x_data, self.y_data, xerr=xError, yerr=yError, ecolor=color, fmt='none')


    def plotCurveFit(self):
        raise NotImplementedError
    

    def setLabels(self, xLabel="x", yLabel="y", title="y vs x"):
        self.ax.set_xlabel(xLabel)
        self.ax.set_ylabel(yLabel)
        self.ax.set_title(title)
    

    def setLimits(self):
        raise NotImplementedError


    def showPlot(self):
        self.ax.legend()