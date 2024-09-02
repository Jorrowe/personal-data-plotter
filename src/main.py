import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from plotter import DataPlotter

def loadData(filePath, sheetName):
    df = pd.read_excel(filePath, sheetName)
    return df["x"].values, df["y"].values


def main():
    try:
        x, y = loadData('test.xlsx', "Sheet4")
        plotter = DataPlotter(x, y)
        
        plotter.plotData(point_size=10, name="Sample Data")
        plotter.plotErrors()
        plotter.plotCurveFit('poly', degree=2)
        
        plotter.setLabels(title="Sample Plot")
        plotter.setLimits()
        plotter.showPlot()

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()